import uuid
class Menu:
    def __init__ (self,name,price):
        self.itemCode = uuid.uuid4()
        self.name = name
        self.price = price
    def get_code(self):
        return self.itemCode
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price