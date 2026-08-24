from abc import ABC,abstractmethod
class Order:
    def __init__ (self):
        self.user = None
        self.restaurant = None
        self.menuItems = []
        self.total = 0
        self.payment = None
        self.schedule = ""
    @abstractmethod
    def get_type():
        pass
    def set_user(self,user):
        self.user = user
    def get_user(self):
        return self.user
    def set_restaurant(self,rest):
        self.restaurant = rest
    def get_restaurant(self):
        return self.restaurant
    def set_payment(self,payment):
        self.payment = payment
    def get_payment(self):
        return self.payment
    def set_total(self):
        total=0
        for items in self.menuItems:
            total += items.get_price()
        self.set_total = total
        return total
    def get_total(self):
        return self.set_total
    def set_items(self,menuI):
        for items in menuI:
            self.menuItems.append(items)
    def get_items(self):
        return self.menuItems
    def set_schedule(self,type):
        self.schedule = type
    def get_schedule(self):
        return self.schedule
    