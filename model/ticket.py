class Ticket:
    def __init__(self, ticket_id, employee_name, issue_type, priority, raised_date, status):
        self.ticket_id = ticket_id
        self.employee_name = employee_name
        self.issue_type = issue_type
        self.priority = priority
        self.raised_date = raised_date
        self.status = status

    def __str__(self):
        return f"{self.ticket_id} {self.employee_name} {self.issue_type} {self.priority} {self.raised_date} {self.status}"
