from fastapi import FastAPI,WebSocket,WebSocketDisconnect
from langchain.chat_models import init_chat_model
import asyncio
from pydantic import BaseModel
from dotenv import load_dotenv
import time
load_dotenv()
#  psql -U postgres
app = FastAPI()
llm = init_chat_model(model="gpt-4o-mini", model_provider="openai")

# vector search 
# memory search
# user search
# model selection

class Payload(BaseModel):
    user_id : str
    query : str

async def vector_search(user_id):
    await asyncio.sleep(0.3)
    return [
        "langchain is the good library for ai"
    ]
async def memory_search(user_id):
    await asyncio.sleep(0.3)
    return "User like to know about AI news"

async def user_info(user_id):
    await asyncio.sleep(0.2)
    return "User name is sameer"

async def model_selection(user_id):
    await asyncio.sleep(0.4)
    return "openai"

@app.websocket("/ws")
async def websocket_connection(ws:WebSocket):
    await ws.accept()
    try:
        while True:
            msg = await ws.receive_text()
            final_msg = f"Your Msg:{msg}"
            await ws.send_text(final_msg)
    except WebSocketDisconnect:
        print("Client disconnected")

@app.websocket("/chat")
async def chat_streaming(ws : WebSocket):
    await ws.accept()
    try:
        while True:
            msg = await ws.receive_text()
            async for chunk in llm.astream(msg):
                print(chunk.content)
                await ws.send_text(chunk.content)
    except WebSocketDisconnect:
        print("Connection Closed")

@app.post("/ask")
async def user_query(payload:Payload):

    #Option One create_task

    # memory_task = asyncio.create_task(memory_search(payload.user_id))
    # vector_task = asyncio.create_task(vector_search(payload.user_id))
    # user_task = asyncio.create_task(user_info(payload.user_id))
    # model_task = asyncio.create_task(model_selection(payload.user_id))

    # #--------------> I can do some task here if required

    # memory = await memory_task
    # vector = await vector_task
    # user = await user_task
    # model = await model_task
    
    #Option 2 gather will do all the task at once

    memory, model, user, vector = await asyncio.gather(
        memory_search(payload.user_id),
        model_selection(payload.user_id),
        user_info(payload.user_id),
        vector_search(payload.user_id)
    )

    final_prompt = f"""
     Following are the details of the user and the query asked create a personalized response for the user:
     User Name :
     {user}
     
     User Query:
     {payload.query}

     Vector Search:
     {vector}
     
     Memory Search:
     {memory}
""" 
    try:
        start = time.time()
        ans = await llm.ainvoke(final_prompt)
        end = time.time()
        total = end-start
        content = ans.content

    except Exception as e:
        print("Root cause of error:", e)
        content = "Sorry, service temporarily unavailable."

    return {
        "user": user,
        "content": content,
        "model":model,
        "execution_time":total
    }



