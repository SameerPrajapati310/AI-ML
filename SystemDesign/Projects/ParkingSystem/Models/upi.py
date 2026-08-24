from Startegy.payementStrategy import PaymentStrategy
class Upi(PaymentStrategy):
    def pay(self):
        print("Payment done using UPI!!!")
    def get_type(self):
        return "Upi"