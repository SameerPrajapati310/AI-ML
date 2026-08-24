class Booking:

    def __init__(
        self,
        booking_id,
        user,
        movie,
        seats,
        total,
        ticket
    ):

        self.booking_id = booking_id
        self.user = user
        self.movie = movie
        self.seats = seats
        self.total = total
        self.ticket = ticket

    def __str__(self):

        return f"""
Booking Successful

Booking Id : {self.booking_id}
Movie      : {self.movie.get_name()}
Seats      : {self.seats}
Total      : ₹{self.total}
"""