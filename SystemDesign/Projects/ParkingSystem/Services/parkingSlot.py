import random
import time
class ParkingSlot:
    def __init__(self,m,n):
        self.m = m
        self.n = n
        self.total_slots = []
        self.create_slots()

    def create_slots(self):
        self.total_slots = [[random.randint(0, 2) for _ in range(self.n)] for _ in range(self.m)]

    def display_slots(self):
        
        print("\nParking Layout")
        print("ENTER ROW COL for booking Slots")
        print("🟩 = Bike   🟦 = Car   ⬛ = Booked\n")


        # Column headers
        print("    ", end="")
        for j in range(len(self.total_slots[0])):
            print(f"{j+1:^3}", end="")
        print()

        for i, row in enumerate(self.total_slots):
            print(f"{i+1:^3}", end=" ")
            for slot in row:
                if slot == 0:
                    print("🟩 ", end="")
                elif slot == 1:
                    print("🟦 ", end="")
                else:
                    print("⬛ ", end="")
            print()
    
    def book_slot_done(self,user):
        ticket = user.get_ticket()
        final_ticket =  ticket.get_ticket(user)
        return "Booking Confirmed!!!"


    
    def check_availability(self,user):
        ticket = user.get_ticket()
        type = ticket.get_type()
        row = ticket.get_row()
        col = ticket.get_col()
        print(">>>>>>>>>",self.total_slots[row][col])
        print("++++++++++",type)
        
        if self.total_slots[row][col] == type:
            print("SLot Available Do you want to Book ticket.")
            return True
        else:
            print("Please select another slot.")
            return False
    
    def get_total(self,user):
        total = 0
        ticket = user.get_ticket()
        vechical_type = ticket.get_type()
        if vechical_type == 1:
            total = 50
        else:
            total = 20

        ticket.set_total(total) 
    def payment_mode(self,payment):
        print("Connecting to Server...")
        time.sleep(1)
        payment.pay()


    
        

    
    
        