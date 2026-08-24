from Strategy.payment import Payment
class UPI(Payment):
    def __init__ (self,mob):
        self.mob = mob
    def pay(self,amount):
        print("Total :", amount)
        print("Mobile Number :", self.mob)