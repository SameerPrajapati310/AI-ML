from Payment.payamentFactory import PaymentFactory
from TicketFactory.ticketFactory import TicketFactory
from Models.booking import Booking

import uuid


class BookingService:

    def book(self, user, payment_type):

        cart = user.get_cart()

        cart.get_total()

        payment = PaymentFactory.payNow(
            payment_type,
            cart.get_total()
        )

        ticket = TicketFactory.select_ticket(
            cart.get_ticket_type()
        )

        payment.pay()

        ticket.book_ticket()

        booking = Booking(
            booking_id=uuid.uuid4(),
            user=user,
            movie=cart.get_movie(),
            seats=cart.get_seat(),
            total=cart.get_total(),
            ticket=ticket
        )

        return booking