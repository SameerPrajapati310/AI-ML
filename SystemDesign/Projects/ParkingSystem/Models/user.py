import uuid
from Models.ticket import Ticket
class User:
    def __init__ (self,name,age):
        self.id = uuid.uuid4()
        self.name = name
        self.age = age
        self.ticket = Ticket()
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_ticket(self):
        return self.ticket