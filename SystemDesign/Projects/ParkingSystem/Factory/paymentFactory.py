from Models.upi import Upi
from Models.cash import Cash
class PaymentFactory:
    @staticmethod
    def payment_type(type):
        if type == "Upi":
            return Upi()
        elif type == "Cash":
            return Cash()
