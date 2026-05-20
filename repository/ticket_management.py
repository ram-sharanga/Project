from util.db_util import DBConnection
from model.ticket import Ticket
from exception.ticket_not_found_exception import TicketNotFoundException

class TicketManagement:
    def __init__(self):
        self.db = DBConnection()
        self.cursor = self.db.get_cursor()

    def add_ticket(self, employee_name, issue_type, priority, raised_date, status):
        try:
            self.cursor.execute(
                "INSERT INTO SupportTickets (employee_name, issue_type, priority, raised_date, status) "
                "VALUES (?, ?, ?, ?, ?)",
                (employee_name, issue_type, priority, raised_date, status)
            )
            self.db.commit()
            return True
        except Exception:
            return False

    def update_priority(self, ticket_id, priority):
        self.cursor.execute(
            "UPDATE SupportTickets SET priority = ? WHERE ticket_id = ?",
            (priority, ticket_id)
        )
        self.db.commit()
        if self.cursor.rowcount == 0:
            raise TicketNotFoundException()
        return True

    def delete_ticket(self, ticket_id):
        self.cursor.execute(
            "DELETE FROM SupportTickets WHERE ticket_id = ?",
            (ticket_id,)
        )
        self.db.commit()
        if self.cursor.rowcount == 0:
            raise TicketNotFoundException()
        return True

    def get_all_tickets(self):
        self.cursor.execute("SELECT * FROM SupportTickets")
        rows = self.cursor.fetchall()
        return [Ticket(*row) for row in rows]

    def search_by_employee_and_status(self, employee_name, status):
        self.cursor.execute(
            "SELECT * FROM SupportTickets WHERE employee_name = ? AND status = ?",
            (employee_name, status)
        )
        rows = self.cursor.fetchall()
        if not rows:
            raise TicketNotFoundException()
        return [Ticket(*row) for row in rows]

    def filter_exclude_issue_and_priority(self, excluded_issue, max_priority):
        self.cursor.execute(
            "SELECT * FROM SupportTickets WHERE issue_type <> ? AND priority <= ?",
            (excluded_issue, max_priority)
        )
        rows = self.cursor.fetchall()
        return [Ticket(*row) for row in rows]

    def close_connection(self):
        self.db.close()
