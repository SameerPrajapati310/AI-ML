class Order:
    def __init__(self, order_id, amount):
        self.order_id = order_id
        self.amount = amount

    def __repr__(self):
        return f"Order(id={self.order_id}, amount={self.amount})"


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.orders = []  # One user can have many orders

    def add_order(self, order):
        self.orders.append(order)

    def show_orders(self):
        print(f"Orders of {self.name}:")

        for order in self.orders:
            print(order)


# Create a user
user = User(1, "Sameer")

# Create multiple orders
order1 = Order(101, 500)
order2 = Order(102, 900)
order3 = Order(103, 300)

# One user -> many orders
user.add_order(order1)
user.add_order(order2)
user.add_order(order3)

# Display
user.show_orders()