"""
A simple definition of the Factory Design Pattern (FDP) is:
"The Factory Design Pattern is a creational design pattern that creates objects for the client, so the client doesn't need to know which concrete class to instantiate."

Or even simpler:
"Factory Pattern hides object creation from the client."

Example

Without Factory:
payment = UPI()
The client knows exactly which object to create.

With Factory:
payment = PaymentFactory.create("UPI")
The client only asks the factory. The factory decides whether to create UPI, CreditCard, or Wallet.

One-line interview definition
"Factory Design Pattern provides a centralized way to create objects while hiding the object creation logic from the client."

"""



from abc import ABC,abstractmethod

class Talkable(ABC):
    @abstractmethod
    def talk(self):
        pass

class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass



class NormalTalk(Talkable):
    def talk(self):
        print("I am normal talking robot")

class NoTalk(Talkable):
    def talk(self):
        print("I am normal talking robot")

class NormalFly(Flyable):
    def fly(self):
        print("I am normal Flying robot")

class NoFly(Flyable):
    def fly(self):
        print("I am no Flying robot :-(")

class Robot:
    def __init__ (self,t,f):
        self.talkable = t
        self.flyable = f
    
    def performTalk(self):
        self.talkable.talk()

    def performFly(self):
        self.flyable.fly()

class RobotSelection(ABC):
    @abstractmethod
    def selection(self):
        pass

class TalkSelection(RobotSelection):
    def __init__ (self,txt):
        self.txt = txt
    def selection(self):
        if self.txt == "Normal":
            return NormalTalk()
        else :
            return NoTalk()

class FlySelection(RobotSelection):
    def __init__ (self,txt):
        self.txt = txt
    def selection(self):
        if self.txt == "Fly":
            return NormalFly()
        else :
            return NoFly()

        

class CompanionRobot(Robot):
    def __init__ (self,t,f):
        print("Companion initialised...") 
        super().__init__(TalkSelection(t).selection(),FlySelection(f).selection())



robot = CompanionRobot("Normal","Fly")

robot.performFly()
robot.performTalk()


# class TalkFactory:
#     @staticmethod
#     def create(kind):
#         if kind == "Normal":
#             return NormalTalk()
#         return NoTalk()


# class FlyFactory:
#     @staticmethod
#     def create(kind):
#         if kind == "Fly":
#             return NormalFly()
#         return NoFly()

# class CompanionRobot(Robot):
#     def __init__(self, t, f):
#         super().__init__(
#             TalkFactory.create(t),
#             FlyFactory.create(f)
#         )