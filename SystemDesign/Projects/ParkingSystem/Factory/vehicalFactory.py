from Models.bike import Bike
from Models.car import Car

class VehicleFactory:
    @staticmethod
    def vechical_type(type):
        if type == "Bike":
            return Bike()
        elif type == "Car":
            return Car()
