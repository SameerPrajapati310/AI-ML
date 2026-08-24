from Model.deliveryOrder import DeliveryOrder
from Model.user import User
from Model.order import Order
from Model.restaurants import Restaurant
from Strategy.payment import Payment
from Model.menu import Menu
class NowOrderFactory:
    def createOrder(self,user : User,restaurant : Restaurant,payment : Payment,menuItems : Menu,totalCost,orderType):
        order = None
        if orderType == "Delivery":
            do = DeliveryOrder()
            do.set_address(user.get_location())
            order = do
        order.set_user(user)
        order.set_restaurant(restaurant)
        order.set_payment(payment)
        order.set_items(menuItems)
        order.set_total()
        return order
        
        
        
