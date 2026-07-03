"""
Agent loop pseudocode, updated to reflect how systems like Cursor Agent
mode actually behave:

1. No rigid upfront plan by default — a single continuous ReAct loop
   (reason -> act -> observe) that plans turn-by-turn. An explicit
   "Plan Mode" path is kept as an opt-in for when you *do* want an
   upfront markdown-style plan with file references.
2. Tool-call budgeting — hard ceiling per run, with a "Max mode" style
   higher ceiling, and a checkpoint/pause when the budget is hit.
3. Parallelism — a dispatcher that can fan a task out to multiple
   worker agents (git-worktree style isolation) and independent
   subagents for side work (tests, docs, research) that run
   concurrently with the main loop.
4. Confirmation / approval gating — risky tool calls (terminal,
   write_file) pause for human approval unless auto-run is enabled.
5. Model routing — picks a model per task/tool type instead of one
   fixed call.
6. Async / background mode — the same loop can run detached, polled
   for status, instead of blocking in a live session.
"""

import uuid
from dataclasses import dataclass, field
from enum import Enum


# ---------------------------
# State
# ---------------------------

class RunMode(Enum):
    INTERACTIVE = "interactive"   # live session, blocking
    BACKGROUND = "background"     # async, cloud/worktree, polled


@dataclass
class AgentState:
    user_request: str
    run_mode: RunMode = RunMode.INTERACTIVE

    # Optional upfront plan (only populated in Plan Mode)
    plan: list = field(default_factory=list)
    plan_mode: bool = False

    context: list = field(default_factory=list)
    history: list = field(default_factory=list)

    files_read: list = field(default_factory=list)
    files_modified: list = field(default_factory=list)

    tool_results: list = field(default_factory=list)
    errors: list = field(default_factory=list)

    # Tool-call budgeting
    tool_call_count: int = 0
    max_tool_calls: int = 25       # standard mode
    max_mode: bool = False         # True -> raise ceiling, drop truncation

    # Approval / autonomy
    auto_run: bool = False         # "YOLO mode" — skip confirmations
    pending_approval: dict | None = None

    # Bookkeeping
    run_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    completed: bool = False
    checkpointed: bool = False

    def __post_init__(self):
        if self.max_mode:
            self.max_tool_calls = 200


# ---------------------------
# Model Router
# ---------------------------
# Cursor doesn't call one fixed model — it routes by task type.
# This keeps the same call_claude-style interface but picks the
# underlying model per call.

MODEL_ROUTES = {
    "plan": "opus",          # architecture / upfront planning
    "reason": "sonnet",      # everyday turn-by-turn reasoning
    "bulk_edit": "composer", # fast multi-file edits
    "research": "sonnet",
}


def route_model(task_type: str) -> str:
    return MODEL_ROUTES.get(task_type, "sonnet")


def call_llm(context, task_type="reason"):
    model = route_model(task_type)
    return call_claude(context, model=model)  # provided by runtime


# ---------------------------
# Optional Planner (Plan Mode only)
# ---------------------------

def planner_llm(user_request):
    """
    Only invoked if the caller explicitly opts into Plan Mode.
    Produces an upfront markdown-style plan with file references,
    which the user can review/edit before execution starts.
    """
    context = {"request": user_request}
    response = call_llm(context, task_type="plan")
    return response.plan_steps  # e.g. list[str] with file refs


# ---------------------------
# Context Retrieval
# ---------------------------

def retrieve_context(state: AgentState):
    relevant_files = semantic_search(state.user_request, state.history)
    return {
        "request": state.user_request,
        "files": relevant_files,
        "history": state.history,
        "tool_results": state.tool_results[-10:],  # recent window only
    }


# ---------------------------
# Approval gating
# ---------------------------

RISKY_TOOLS = {"terminal", "write_file"}


def needs_approval(tool_call, state: AgentState) -> bool:
    if state.auto_run:
        return False
    return tool_call.name in RISKY_TOOLS


def request_approval(tool_call, state: AgentState):
    """
    In INTERACTIVE mode this blocks on a human decision.
    In BACKGROUND mode this queues the approval and pauses the run;
    a separate poll/resume call picks it back up.
    """
    state.pending_approval = {"tool_call": tool_call}
    if state.run_mode == RunMode.INTERACTIVE:
        return await_human_decision(tool_call)  # blocking prompt
    else:
        state.checkpointed = True
        return None  # caller must resume() later


# ---------------------------
# Tool Execution
# ---------------------------

def execute_tool(tool_call, state: AgentState):
    if needs_approval(tool_call, state):
        decision = request_approval(tool_call, state)
        if decision != "approved":
            return ToolResult(name=tool_call.name, rejected=True)
        state.pending_approval = None

    if tool_call.name == "read_file":
        result = read_file(tool_call.path)
        state.files_read.append(tool_call.path)
        return result

    elif tool_call.name == "write_file":
        result = write_file(tool_call.path, tool_call.content)
        state.files_modified.append(tool_call.path)
        return result

    elif tool_call.name == "terminal":
        return run_terminal(tool_call.command)

    elif tool_call.name == "search":
        return semantic_search(tool_call.query)

    elif tool_call.name == "spawn_subagent":
        # Fire-and-continue: subagent runs concurrently, reports
        # back into state.tool_results when done (see dispatch below).
        return spawn_subagent(tool_call.task, parent_state=state)


# ---------------------------
# Verification
# ---------------------------

def verify():
    result = run_tests()
    return (not result.failed), result


# ---------------------------
# Single continuous ReAct loop
# ---------------------------
# No per-step plan advancement. The loop reasons, acts, observes,
# and decides for itself when the overall request is satisfied —
# unless Plan Mode produced a checklist, in which case the loop still
# runs continuously but treats the plan as reference context rather
# than a rigid state machine to walk through.

def run_agent_loop(state: AgentState):

    if state.plan_mode and not state.plan:
        state.plan = planner_llm(state.user_request)
        state.context.append({"plan": state.plan})

    while not state.completed:

        # --- Tool-call budget check ---
        if state.tool_call_count >= state.max_tool_calls:
            state.checkpointed = True
            return checkpoint_and_ask_to_continue(state)

        context = retrieve_context(state)
        if state.plan:
            context["plan"] = state.plan

        response = call_llm(context, task_type="reason")

        if response.has_tool_call():
            state.tool_call_count += 1

            tool_result = execute_tool(response.tool_call, state)
            state.tool_results.append(tool_result)

            if state.checkpointed:
                # Waiting on async approval in background mode
                return state

            continue

        if response.has_patch():
            apply_patch(response.patch)
            state.files_modified.append(response.patch.path)

            success, result = verify()
            if success:
                state.history.append(response.summary)
            else:
                state.errors.append(result)
                state.tool_results.append(result)
                continue  # keep reasoning, don't advance a "step"

        if response.is_task_complete():
            state.completed = True

    return state


# ---------------------------
# Parallel dispatch (multi-agent / subagents)
# ---------------------------
# Fans a request out across isolated worktree-style agents, and/or
# spins off subagents for side work that runs concurrently with the
# main loop instead of blocking it.

MAX_PARALLEL_AGENTS = 8


def dispatch_parallel(user_requests: list[str]):
    """
    One AgentState + run_agent_loop per request, isolated on its own
    branch/worktree, run concurrently up to MAX_PARALLEL_AGENTS.
    """
    batch = user_requests[:MAX_PARALLEL_AGENTS]
    states = [AgentState(user_request=r, run_mode=RunMode.BACKGROUND) for r in batch]
    return run_concurrently([lambda s=s: run_agent_loop(s) for s in states])


def spawn_subagent(task: str, parent_state: AgentState):
    """
    Side work (tests, docs, research) that runs concurrently with the
    main loop and reports back asynchronously rather than blocking it.
    """
    sub_state = AgentState(user_request=task, run_mode=RunMode.BACKGROUND)
    future = run_async(lambda: run_agent_loop(sub_state))
    return {"subagent_task": task, "future": future}


# ---------------------------
# Entry points
# ---------------------------

def run_agent(user_request, plan_mode=False, auto_run=False, max_mode=False):
    """Interactive, blocking entry point (default IDE-session behavior)."""
    state = AgentState(
        user_request=user_request,
        run_mode=RunMode.INTERACTIVE,
        plan_mode=plan_mode,
        auto_run=auto_run,
        max_mode=max_mode,
    )
    final_state = run_agent_loop(state)
    return generate_final_summary(final_state)


def run_agent_background(user_request, plan_mode=False):
    """
    Async entry point (cloud/background agent). Returns immediately
    with a run_id; caller polls status or resumes past approval
    checkpoints separately.
    """
    state = AgentState(
        user_request=user_request,
        run_mode=RunMode.BACKGROUND,
        plan_mode=plan_mode,
        auto_run=True,  # background agents typically auto-run
    )
    submit_async(lambda: run_agent_loop(state))
    return state.run_id


def resume(run_id, decision="approved"):
    """Resume a checkpointed background run after an approval or budget pause."""
    state = load_state(run_id)
    if state.pending_approval:
        state.pending_approval["decision"] = decision
        state.pending_approval = None
    state.checkpointed = False
    return run_agent_loop(state)