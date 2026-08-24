from Models.movie import Movie
from Models.availableMovie import AvailableMovies
from Payment.payamentFactory import PaymentFactory
from TicketFactory.ticketFactory import TicketFactory
from Models.bookingService import BookingService

class TicketBookingPlatform:
    def __init__(self):
        self.available = AvailableMovies()
        self.booking_service = BookingService()
        self.start_service()

    def start_service(self):
        self.available.add_movies(Movie("Avengers", 100))
        self.available.add_movies(Movie("Iron Man", 120))
        self.available.add_movies(Movie("Spider-Man: No Way Home", 150))
        self.available.add_movies(Movie("Batman", 110))
        self.available.add_movies(Movie("The Dark Knight", 130))
        self.available.add_movies(Movie("Inception", 140))
        self.available.add_movies(Movie("Interstellar", 160))
        self.available.add_movies(Movie("John Wick", 125))
        self.available.add_movies(Movie("Mission Impossible", 145))
        self.available.add_movies(Movie("Top Gun: Maverick", 170))
        self.available.add_movies(Movie("The Matrix", 135))
        self.available.add_movies(Movie("Joker", 115))
        self.available.add_movies(Movie("Doctor Strange", 155))
        self.available.add_movies(Movie("Black Panther", 150))
        self.available.add_movies(Movie("Thor: Ragnarok", 140))
        self.available.add_movies(Movie("Captain America: Civil War", 130))
        self.available.add_movies(Movie("Avatar", 180))
        self.available.add_movies(Movie("Titanic", 160))
        self.available.add_movies(Movie("The Lion King", 100))
        self.available.add_movies(Movie("Kung Fu Panda", 90))


    def select_movie(self, user, movie_name):

        movie = self.available.search_movie(movie_name)

        cart = user.get_cart()

        cart.set_movie(movie)

    def select_seats(self, user, seats):

        cart = user.get_cart()

        cart.set_seats(seats)

    def select_ticket(self, user, ticket_type):

        cart = user.get_cart()

        cart.set_ticket_type(ticket_type)

    def checkout(self, user, payment_type):

        return self.booking_service.book(
            user,
            payment_type
        )
    


        

        


        




