import uuid
class Seats:
    def __init__ (self,user):
        self.seat_id = uuid.uuid4()
        self.seats = 0
    def select_seats(self,count):
        self.seats = count
    def get_seats(self):
        return self.seats
