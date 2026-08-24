from abc import ABC,abstractmethod
class OrderFactory:
    @abstractmethod
    def createOrder(user,restaurant,payment,menuItems,totalCost,orderType):
        pass