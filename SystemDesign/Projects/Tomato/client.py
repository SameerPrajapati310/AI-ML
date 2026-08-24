from tom import Tom
from Model.user import User
from Strategy.Upi import UPI

tomato = Tom()

user_one = User("Sameer","Delhi")

print("UserName :", user_one.get_name(), "User is active")

location = input("Please enter the location from where u wnat to Oder:\n")

list_restaurant = tomato.search_restaurant(location)
for items in list_restaurant:
    print("Name of restaurant :", items.get_name())
select_rest = input("Select restaurant :")
selected_rest = None

for items in list_restaurant:
    if select_rest == items.get_name():
        selected_rest = items
        break
print("Selected restaurant:",selected_rest.get_name())
print("Menu Items :")

tomato.set_restaurant(user_one,selected_rest)

count = 0
print(list_restaurant)
for items in list_restaurant:
    if selected_rest.get_name() == items.get_name():
        print("================")
        for elements in items.get_menu(): 
            print("Name :", elements.get_name(), "| Price :", elements.get_price())
        print("================")
        print("ADD items to cart, Enter q to exit")
        while True:
            name = input("Enter Item Name: ")

            if name.lower() == "q":
                break

            found = False

            for element in items.get_menu():
                if element.get_name().lower() == name.lower():
                    tomato.add_cart(user_one, element.get_code())
                    print(f"{element.get_name()} added to cart.")
                    found = True
                    break

            if not found:
                print("Item not found.")
print("================")
tomato.printUserCart(user_one)


print("Checking Out>>>")
order = tomato.checkOutNow(user_one,"Delivery",UPI("1234567890"))

            
            
            






