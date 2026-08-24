from Services.parkingLotService import ParkingLotService
from Models.user import User

user = User("Sameer",25)
ticket = user.get_ticket()
manager = ParkingLotService()

manager.display_slots()
print("Enter Vehicle Type :")
type = input()
ticket.set_type(type)

row = input("Select Row :")
col = input("Select Col :")
ticket.set_row(int(row)-1)
ticket.set_col(int(col)-1)
manager.check_availability(user)

y_n = input("Yes / No :")
print()
if y_n == "Yes":
    manager.book_slot(user)
else:
    print("Visit again!!!")


print("Select Payment Mode : UPI/Cash")
mode = input()
manager.payement_mode(mode)
manager.get_recipt(user,mode)
