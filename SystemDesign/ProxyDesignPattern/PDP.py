from abc import ABC, abstractmethod

class IRealImage(ABC):
    @abstractmethod
    def display(self):
        pass

class RealImage(IRealImage):
    def __init__ (self,path):
        self.path = path
        print("[[Loading heavy operations...]]")
    def display(self):
        print(f"Here is your Image: {self.path}")

class Proxy(IRealImage):
    def __init__(self,path):
        self.path = path
        self.filename = None

    def display(self):
        if self.filename == None:
            self.filename = RealImage(self.path)
        self.filename.display()

if __name__ == "__main__":
    img = Proxy("123")
    img.display()
    