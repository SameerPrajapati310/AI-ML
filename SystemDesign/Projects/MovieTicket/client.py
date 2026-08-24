from main import TicketBookingPlatform
from Models.user import User

manager = TicketBookingPlatform()

user = User("Sameer", 20)

print("\n========== Movie Ticket Booking ==========\n")

print("Available Movies:")
print("-------------------------------")

for movie in manager.available.get_movies():
    print(f"{movie.get_name()}  -  ₹{movie.get_price()}")

print()

movie_name = input("Enter Movie Name: ")
manager.select_movie(user, movie_name)

seats = int(input("Enter Number of Seats: "))
manager.select_seats(user, seats)

print("\nSelect Ticket Type")
print("1. Premium")
print("2. Normal")

ticket_choice = input("Enter Choice: ")

if ticket_choice == "1":
    manager.select_ticket(user, "Premium")
else:
    manager.select_ticket(user, "Normal")

print("\nSelect Payment Method")
print("1. UPI")
print("2. Cash")

payment_choice = input("Enter Choice: ")

if payment_choice == "1":
    payment_type = "UPI"
else:
    payment_type = "Cash"

booking = manager.checkout(
    user,
    payment_type
)

print("\n========== Booking Successful ==========")
print(booking)