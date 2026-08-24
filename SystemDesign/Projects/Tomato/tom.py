
from Model.restaurants import Restaurant
from Model.menu import Menu
from Manager.resturantManager import RestaurantManager
from Model.deliveryOrder import DeliveryOrder
from Model.user import User
from Model.order import Order
from Model.restaurants import Restaurant
from Strategy.payment import Payment
from Model.menu import Menu
from OrderFactory.NowOrderFactory import NowOrderFactory
class Tom:
    def __init__(self):
        self.start_rest()
    def start_rest(self):
        manager = RestaurantManager()

        # ---------------- Restaurant 1 ----------------
        restaurant_one = Restaurant("Burger King", "Delhi")
        restaurant_one.add_menu(Menu("Whopper", 199))
        restaurant_one.add_menu(Menu("Veg Whopper", 179))
        restaurant_one.add_menu(Menu("French Fries", 99))
        restaurant_one.add_menu(Menu("Coke", 60))

        # ---------------- Restaurant 2 ----------------
        restaurant_two = Restaurant("KFC", "Mumbai")
        restaurant_two.add_menu(Menu("Zinger Burger", 229))
        restaurant_two.add_menu(Menu("Hot Wings", 189))
        restaurant_two.add_menu(Menu("Chicken Bucket", 599))
        restaurant_two.add_menu(Menu("Pepsi", 70))

        # ---------------- Restaurant 3 ----------------
        restaurant_three = Restaurant("Domino's", "Bangalore")
        restaurant_three.add_menu(Menu("Margherita Pizza", 249))
        restaurant_three.add_menu(Menu("Farmhouse Pizza", 459))
        restaurant_three.add_menu(Menu("Garlic Bread", 159))
        restaurant_three.add_menu(Menu("Choco Lava Cake", 129))

        # ---------------- Restaurant 4 ----------------
        restaurant_four = Restaurant("McDonald's", "Hyderabad")
        restaurant_four.add_menu(Menu("McAloo Tikki", 69))
        restaurant_four.add_menu(Menu("McSpicy Paneer", 219))
        restaurant_four.add_menu(Menu("French Fries", 109))
        restaurant_four.add_menu(Menu("McFlurry", 119))

        # ---------------- Restaurant 5 ----------------
        restaurant_five = Restaurant("Pizza Hut", "Chennai")
        restaurant_five.add_menu(Menu("Veggie Supreme", 499))
        restaurant_five.add_menu(Menu("Chicken Supreme", 599))
        restaurant_five.add_menu(Menu("Cheesy Garlic Bread", 179))
        restaurant_five.add_menu(Menu("Pepsi", 60))

        # ---------------- Restaurant 6 ----------------
        restaurant_six = Restaurant("Subway", "Pune")
        restaurant_six.add_menu(Menu("Veg Delight Sub", 199))
        restaurant_six.add_menu(Menu("Paneer Tikka Sub", 269))
        restaurant_six.add_menu(Menu("Chicken Teriyaki Sub", 329))
        restaurant_six.add_menu(Menu("Cookies", 50))

        # ---------------- Restaurant 7 ----------------
        restaurant_seven = Restaurant("Biryani Blues", "Delhi")
        restaurant_seven.add_menu(Menu("Chicken Biryani", 299))
        restaurant_seven.add_menu(Menu("Veg Biryani", 249))
        restaurant_seven.add_menu(Menu("Raita", 40))
        restaurant_seven.add_menu(Menu("Gulab Jamun", 60))

        manager.add_restaurant(restaurant_seven)

        # Add restaurants to manager
        manager.add_restaurant(restaurant_one)
        manager.add_restaurant(restaurant_two)
        manager.add_restaurant(restaurant_three)
        manager.add_restaurant(restaurant_four)
        manager.add_restaurant(restaurant_five)
        manager.add_restaurant(restaurant_six)
    def search_restaurant(self,location):
        return RestaurantManager.search_by_location(location)
    def set_restaurant(self,user,rest):
        try:
            cart = user.get_cart()
            cart.set_restaurant(rest)
        except Exception as e:
            print("An error occured while setting rest",e)
    def add_cart(self,user,item_code):
        restaurant = user.get_cart().get_restaurant()

        for items in restaurant.get_menu():
            if items.get_code() == item_code:
                user.get_cart().add_item(items)
                break
    def printUserCart(self,user):
        for items in user.get_cart().get_items():
            print("Item Code : ",items.get_code(),"|","Item Name :", items.get_name(), "|", "Item Price :",items.get_price())
        print("====================")
        print("Total", user.get_cart().get_total())

    def checkOutNow(self,user,order_type,paymentMode):
        ans = self.checkOut(user,order_type,paymentMode,NowOrderFactory())
        return ans
    def checkOut(self,user,order_type,paymentMode,order_Factory):
        cart = user.get_cart()
        orderedRestaurant   = cart.get_restaurant()
        itemsordered = cart.get_items()
        totalCost = cart.get_total()
        order = order_Factory.createOrder(user,orderedRestaurant,paymentMode,itemsordered,totalCost,order_type)
        print("Order created")
        print("\n========== ORDER ==========")
        print("Customer   :", order.get_user().get_name())
        print("Restaurant :", order.get_restaurant().get_name())
        print("Type       :", order.get_type())
        print("Payment    :", type(order.get_payment()).__name__)

        print("\nItems:")
        for item in order.get_items():
            print(f" - {item.get_name()} : ₹{item.get_price()}")

        print("Total      : ₹", order.get_total())




