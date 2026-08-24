

from TicketFactory.ticketInterface import TicketInterface
class NormalTicket(TicketInterface):
    def book_ticket(self):
        print("Normal Ticket Booked")