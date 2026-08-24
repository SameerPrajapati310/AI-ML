from TicketFactory.normalTicket import NormalTicket
from TicketFactory.premiumTicket import PremiumTicket
class TicketFactory:
    @staticmethod
    def select_ticket(type):
        if type == "Normal":
            return NormalTicket()
        else:
            return PremiumTicket()