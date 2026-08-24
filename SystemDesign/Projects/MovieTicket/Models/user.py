import uuid
from Models.ticket_cart import TicketCart
class User:
    def __init__ (self,name,age):
        self.id = uuid.uuid4()
        self.name = name
        self.age = age
        self.cart = TicketCart()
    def get_cart(self):
        return self.cart
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_userid(self):
        return self.id