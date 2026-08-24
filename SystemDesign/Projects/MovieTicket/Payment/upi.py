from Payment.paymentInterface import Payment
class UPI(Payment):
    def __init__ (self,number):
        self.number = number
    def get_number(self):
        return self.number
    def pay(self):
        print(f"Payment Sucessfull via UPI :{self.number[0:3]}XXXXXX")
