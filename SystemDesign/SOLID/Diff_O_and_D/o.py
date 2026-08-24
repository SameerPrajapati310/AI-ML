# Here we've achieved Open/Closed Principle because we can add 
# new payment methods by creating new classes.
# However, Checkout still depends on concrete classes, 
# so it violates DIP.


from abc import ABC, abstractmethod

# Abstraction
class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass


# Implementations
class UPI(Payment):

    def pay(self):
        print("UPI Payment")




class CreditCard(Payment):

    def pay(self):
        print("Credit Card Payment")


# High Level Module
class Checkout:

    def checkout(self, payment_type):

        if payment_type == "upi":
            payment = UPI()              # Depends on concrete class

        elif payment_type == "card":
            payment = CreditCard()       # Depends on concrete class

        payment.pay()


checkout = Checkout()
checkout.checkout("upi")