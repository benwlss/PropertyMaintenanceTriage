#split ticket into each individual part
class MaintenanceTicket:
    def __init__(self, ticket_id, address, issue_description, reported_date):
        self.ticket_id = ticket_id
        self.address = address
        self.issue_description = issue_description
        self.reported_date = reported_date
