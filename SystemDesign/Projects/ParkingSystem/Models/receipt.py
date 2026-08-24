from datetime import datetime
from Factory.paymentFactory import PaymentFactory

class Receipt:

    @staticmethod
    def create_receipt(user, payment):
        ticket = user.get_ticket()

        mode =  PaymentFactory.payment_type(payment).get_type()
        print("\n" + "=" * 50)
        print("              PARKING RECEIPT")
        print("=" * 50)

        print(f"Receipt ID    : {ticket.get_id()}")
        print(f"Date & Time   : {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")

        print("\nCustomer Details")
        print("-" * 50)
        print(f"Name          : {user.get_name()}")
        print(f"Age           : {user.get_age()}")

        print("\nParking Details")
        print("-" * 50)
        print(f"Vehicle Type  : {user.get_ticket().get_type()}")
        print(f"Slot          : Row {user.get_ticket().get_row() + 1}, Column {user.get_ticket().get_col() + 1}")

        print("\nPayment Details")
        print("-" * 50)
        print(f"Payment Mode  : {payment}")
        print(f"Amount Paid   : ₹{user.get_ticket().get_total()}")

        print("=" * 50)
        print(f"       Payment Successful via :{mode} ✅")
        print("       Thank You! Visit Again 🚗")
        print("=" * 50)