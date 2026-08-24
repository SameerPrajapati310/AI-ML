"""
"Strategy Pattern lets you choose and combine interchangeable behaviors at runtime."
Robot example

There are three independent strategies.

Robot
 │
 ├── Walk Strategy
 ├── Talk Strategy
 └── Fly Strategy

Example 1:

Walk  → NormalWalk
Talk  → NormalTalk
Fly   → NoFly

Example 2:

Walk  → NoWalk
Talk  → NormalTalk
Fly   → NormalFly

Example 3:

Walk  → NormalWalk
Talk  → NoTalk
Fly   → NormalFly

You are composing the robot from different strategies.

"""


from abc import ABC, abstractmethod


# ---------------- Strategy Interface for Walk ----------------
class WalkableRobot(ABC):
    @abstractmethod
    def walk(self):
        pass


class NormalWalk(WalkableRobot):
    def walk(self):
        print("Walking normally...")


class NoWalk(WalkableRobot):
    def walk(self):
        print("Cannot walk.")


# ---------------- Strategy Interface for Talk ----------------
class TalkableRobot(ABC):
    @abstractmethod
    def talk(self):
        pass


class NormalTalk(TalkableRobot):
    def talk(self):
        print("Talking normally...")


class NoTalk(TalkableRobot):
    def talk(self):
        print("Cannot talk.")


# ---------------- Strategy Interface for Fly ----------------
class FlyableRobot(ABC):
    @abstractmethod
    def fly(self):
        pass


class NormalFly(FlyableRobot):
    def fly(self):
        print("Flying normally...")


class NoFly(FlyableRobot):
    def fly(self):
        print("Cannot fly.")


# ---------------- Robot Base Class ----------------
class Robot(ABC):
    def __init__(self, walk_behavior, talk_behavior, fly_behavior):
        self.walk_behavior = walk_behavior
        self.talk_behavior = talk_behavior
        self.fly_behavior = fly_behavior

    def walk(self):
        self.walk_behavior.walk()

    def talk(self):
        self.talk_behavior.talk()

    def fly(self):
        self.fly_behavior.fly()

    @abstractmethod
    def projection(self):
        pass


# ---------------- Concrete Robot Types ----------------
class CompanionRobot(Robot):
    def projection(self):
        print("Displaying friendly companion features...")


class WorkerRobot(Robot):
    def projection(self):
        print("Displaying worker efficiency stats...")


# ---------------- Main ----------------
if __name__ == "__main__":

    robot1 = CompanionRobot(
        NormalWalk(),
        NormalTalk(),
        NoFly()
    )

    robot1.walk()
    robot1.talk()
    robot1.fly()
    robot1.projection()

    print("-" * 30)

    robot2 = WorkerRobot(
        NoWalk(),
        NoTalk(),
        NormalFly()
    )

    robot2.walk()
    robot2.talk()
    robot2.fly()
    robot2.projection()