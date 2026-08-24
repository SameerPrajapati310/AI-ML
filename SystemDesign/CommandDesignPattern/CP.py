"""
                         RemoteController
                                |
               +----------------+----------------+
               |                                 |
            buttons                         buttonPressed
               |                                 |
       +-------+-------+-------+-------+   +------+------+------+------+
       |       |       |       |       |   |      |      |      |
       v       v       v       v       |   v      v      v      v
      [0]     [1]     [2]     [3]       false  false  false  false
       |       |       |
       |       |       +----> nullptr
       |       |
       |       +-----> FanCommand
       |                  |
       |                  +---- execute()
       |                  |       |
       |                  |       +----> fan->on()
       |                  |
       |                  +---- undo()
       |                          |
       |                          +----> fan->off()
       |
       +------> LightCommand
                  |
                  +---- execute()
                  |       |
                  |       +----> light->on()
                  |
                  +---- undo()
                          |
                          +----> light->off()


"""
from abc import ABC,abstractmethod

class Command:
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class Light:
    def on(self):
        print("Light On")
    def off(self):
        print("Light Off")

class Fan:
    def on(self):
        print("Fan On")
    def off(self):
        print("Fan Off")

class LightCommand(Command):
    def __init__(self,type):
        self.light = type
    def execute(self):
        self.light.on()
    def undo(self):
        self.light.off()

class FanCommand(Command):
    def __init__(self,type):
        self.fan = type
    def execute(self):
        self.fan.on()
    def undo(self):
        self.fan.off()

class Remote:
    def __init__(self):
        self.count = 4
        self.buttons = [None]*self.count
        self.buttonPressed = [False]*self.count
    def set_state(self,idx,object):
        if idx >= 0 and self.buttonPressed[idx] == False:
            self.buttons[idx] = object
    def PressButton(self,idx):
        if idx >= 0 and self.buttons[idx] != None and self.buttonPressed[idx] == False:
            self.buttons[idx].execute()
        elif idx >= 0 and self.buttons[idx] !=  None and self.buttonPressed[idx] == True:
            self.buttons[idx].undo()
        else:
            print("Button not selected")
        self.buttonPressed[idx] = not self.buttonPressed[idx] 
        



bedroom = Light()
celling = Fan()

remote = Remote()
remote.set_state(0,LightCommand(bedroom))
remote.set_state(1,FanCommand(celling))


remote.PressButton(0)
remote.PressButton(0)

remote.PressButton(1)
remote.PressButton(1)

remote.PressButton(2)

# remote.PressButton(2)


    