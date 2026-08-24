class OrderManager:
    _instance = None

    def __init__(self):
        self.order_list = []

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def add_order(self, order):
        self.order_list.append(order)

    def list_orders(self):
        print("\n--- All Orders ---")
        for order in self.order_list:
            print(
                f"User: {order.get_user().get_name()} | "
                f"Total: ₹{order.get_total()}"
            )