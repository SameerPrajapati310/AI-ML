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

    def __init__(self, payment: Payment):
        self.payment = payment

    def checkout(self):
        self.payment.pay()


payment = UPI()
checkout = Checkout(payment)
checkout.checkout()