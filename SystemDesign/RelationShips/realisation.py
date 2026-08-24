from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def fly(self):
        pass

class Bird(Animal):
    def fly(self):
        print('Bird can fly')

class Plane(Animal):
    def fly(self):
        print('Plane can also fly')


p = Plane()
p.fly()

b = Bird()
b.fly()