"""
Write a class Train which has methods to book a ticket, get status(no. of seats) and get fare information
of train running under indian railways.
"""

from random import randint


class Train:

    def __init__(self, train_no):
        self.train_no = train_no

    def book_tickets(self, fro, to):
        self.no_of_tickets = int(input("Enter number of tickets you want to book: "))
        print(
            f"You have booked {self.no_of_tickets} tickets for train no. {self.train_no}, from {fro} to {to}"
        )

    def get_status(self):
        print(f"Train no. {self.train_no} is running!")

    def fare_info(self, fro, to):
        print(
            f"Ticket fare in train no. {self.train_no} from {fro} to {to} is {randint(222, 5555)}"
        )


passenger1 = Train(12399)
passenger1.book_tickets("Delhi", "Vrindavan")
passenger1.get_status()
passenger1.fare_info("Delhi", "Vrindavan")
