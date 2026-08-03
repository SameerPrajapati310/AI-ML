#Single responsibilty principle
#one class should have only one methord 
# it can have multiple methord but it must serve the same purpose
"""
Product → Only if product information changes.
ShoppingCart → Only if cart behavior changes.
Invoice → Only if invoice generation or printing changes.

Since each class has one reason to change, your design follows the Single Responsibility Principle.

A -> hb
e -> hc
  - p,p,p
i -> ibpc
P -> s,d
  - runtm po
  - d ->(vf) -> , (pvf)


"""


class Product:
    def __init__ (self,name,price):
        self.name = name
        self.price = price
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price

class ShoppingCart:
    def __init__ (self):
        self.product = []
    
    def get_product(self):
        return self.product
    
    def add_to_cart(self,p):
        self.product.append(p)
    def get_total(self):
        total = 0
        for i in range(len(self.product)):
            total += self.product[i].get_price()
        return total
class Invoice:
    def __init__ (self,cart):
        self.cart = cart
    def print_invoice(self):
        for prod in self.cart.get_product():
            print("Name",prod.get_name())
            print("Price",prod.get_price())
            print("---------------------")
        
        print("Total: ",self.cart.get_total())

cart = ShoppingCart()
cart.add_to_cart(Product("Laptop",10000))
cart.add_to_cart(Product("Mouse",100))

p = Invoice(cart)
p.print_invoice()