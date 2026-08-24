from Strategy.payment import Payment

class CreditCard:
    def __init__ (self,card):
        self.cardNo = card
    def pay(self,amount):
        print("Total :", amount)
        print("Card Number :", self.cardNo[0:3],"XXXXXX")