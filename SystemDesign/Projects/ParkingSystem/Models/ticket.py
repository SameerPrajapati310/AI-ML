import uuid
class Ticket:
    def __init__ (self):
        self.id = uuid.uuid4()
        self.type = None
        self.row = None
        self.col = None
        self.total = None
    def get_id(self):
        return self.id
    def set_type(self,type):
        if type == "Bike":
            self.type = 0
        else:
            self.type = 1
    def set_row(self,row):
        self.row = row 
    def set_col(self,col):
        self.col = col
    def get_type(self):
        return self.type
    def get_row(self):
        return self.row 
    def get_col(self):
        return self.col
    def set_total(self,amount):
        self.total = amount
    def get_total(self):
        return self.total
    def get_ticket(self, user):
        print("\n" + "=" * 40)
        print("         PARKING TICKET")
        print("=" * 40)
        print(f"Ticket ID    : {self.id}")
        print(f"Customer     : {user.get_name()}")
        print(f"Age          : {user.get_age()}")
        print(f"Vehicle Type : {self.type}")
        print(f"Parking Slot : Row {self.row + 1}, Column {self.col + 1}")
        print("=" * 40)
