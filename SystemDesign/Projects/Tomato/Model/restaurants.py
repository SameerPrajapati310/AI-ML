import uuid
class Restaurant:
    def __init__ (self,name,location):
        self.uid = uuid.uuid4()
        self.name = name
        self.location = location
        self.menu = []
    def get_name(self):
        return self.name
    def get_location(self):
        return self.location
    def add_menu(self,menu):
        self.menu.append(menu)
    def set_restaurant(self,restaurant):
        print("Restaurant Selected :", restaurant)
        self.name = restaurant
        return self.name
    def get_menu(self):
        return self.menu 
    