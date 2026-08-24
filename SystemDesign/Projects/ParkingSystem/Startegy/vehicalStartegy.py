from abc import ABC,abstractmethod
class VehicalStrategy:
    @abstractmethod
    def select_vehicle(self,type):
        pass