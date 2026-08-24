from Services.parkingSlot import ParkingSlot
from Models.receipt import Receipt
from Factory.paymentFactory import PaymentFactory
import time
class ParkingLotService:
    def __init__ (self):
        self.slot = ParkingSlot(4,4)
    def display_slots(self):
        return self.slot.display_slots()
    def check_availability(self,user):
        return self.slot.check_availability(user)
    def book_slot(self,user):
        self.slot.book_slot_done(user)
    def payement_mode(self,payment):
        print("Processing Payment...")
        time.sleep(0.5)
        mode = PaymentFactory.payment_type(payment)
        self.slot.payment_mode(mode)
    def get_recipt(self,user,payment):
        Receipt.create_receipt(user,payment)

        
    
    

