import uuid
class Movie:
    def __init__ (self,name,price):
        self.id = uuid.uuid4()
        self.name = name
        self.price = price
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
    
    