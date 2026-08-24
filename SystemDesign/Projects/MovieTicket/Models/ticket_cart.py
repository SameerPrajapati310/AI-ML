from Models.seates import Seats
from Models.movie import Movie

class TicketCart:
    def __init__ (self):
        self.seat = None
        self.movie = None
        self.ticket_type = None
    def get_total(self):
        total = 0
        if self.movie == None:
            print("Please Select a movie")
            return 
        total += self.movie.get_price()

        if self.seat == None:
            return total
        else:
            total += total*(int(self.seat))
        return total
    def set_ticket_type(self,type):
        self.ticket_type = type
    def get_ticket_type(self):
        return self.ticket_type
    def set_movie(self,movie_name):
        self.movie = movie_name
    def set_seats(self,seat):
        self.seat = seat
    def get_movie(self):
        return self.movie
    def get_seat(self):
        return self.seat

