from Model.order import Order
from abc import ABC,abstractmethod
class DeliveryOrder(Order):
    def __init__ (self):
        super().__init__() 
        self.address = ""
    @abstractmethod
    def get_type(self):
        return "Delivery"
    def set_address(self,add):
        self.address = add
    def get_address(self):
        return self.address

