from Startegy.payementStrategy import PaymentStrategy
class Cash(PaymentStrategy):
    def select_payment(self):
        print("Payment done using Cash!!!")