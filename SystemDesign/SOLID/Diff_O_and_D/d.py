"""
Dependency Inversion is the SOLID principle that high-level modules should depend on abstractions rather than concrete implementations. 
Dependency Injection is one technique used to supply those implementations from outside the class, helping achieve Dependency Inversion.

So your intuition is correct that they usually appear together. 
The subtle but important distinction is:

DIP = "Depend on Payment, not UPI." (design principle)
DI = "Pass the UPI object into Checkout instead of creating it inside." (implementation technique)

"""


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