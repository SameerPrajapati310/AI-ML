
class Animal:
    def __init__ (self,animal):
        self.animal = animal
    def sound(self):
        print(f'{self.animal} makes sound')

class Dog(Animal):
    def __init__ (self,animal):
        self.animal = animal
    def sound(self):
        print(f'{self.animal} Barks')

class Cat(Animal):
    def __init__ (self,animal):
        self.animal = animal
    def sound(self):
        print(f'{self.animal} Meows')

c = Cat('kitty')
d = Dog('Bruno')
c.sound()
d.sound()