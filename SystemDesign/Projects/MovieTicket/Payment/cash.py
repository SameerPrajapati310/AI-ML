from Payment.paymentInterface import Payment
class Cash(Payment):
    def __init__ (self,amount):
        self.amount = amount
    def get_number(self):
        return self.amount
    def pay(self):
        print(f"Payment Sucessfull via Cash :{self.amount}")
