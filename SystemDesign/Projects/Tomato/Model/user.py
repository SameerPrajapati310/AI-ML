from Model.cart import Cart
import uuid
class User:
    def __init__ (self,name,location):
        self.user_id = uuid.uuid4()
        self.user_name = name
        self.user_location = location
        self.cart = Cart()
    def get_name(self):
        return self.user_name
    def get_location(self):
        return self.user_location
    def get_cart(self):
        return self.cart