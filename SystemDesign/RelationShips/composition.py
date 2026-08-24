' This is a stronger form in the obeject is only alive during the parent class ression'

class Engine:
    def __init__ (self):
        print('Engine installed')

class Car:
    def __init__ (self, name):
        self.name = name
        self.engine = Engine()
    def create_car(self):
        print(f'{self.name} car created!!!')


c = Car('Tata')
c.create_car()