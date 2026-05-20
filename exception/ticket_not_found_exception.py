class TicketNotFoundException(Exception):
    def __init__(self):
        super().__init__("Ticket not found. Please check the ticket ID, employee name, or status.")
