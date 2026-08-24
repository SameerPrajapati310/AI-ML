from Payment.upi import UPI
from Payment.cash import Cash
class PaymentFactory:
    @staticmethod
    def payNow(type,amount):
        if type == "UPI":
            return UPI(amount)
        else:
            return Cash(amount)
