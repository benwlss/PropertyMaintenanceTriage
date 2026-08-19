from decision import priority_choice, contractor_choice


class MaintenanceTicket:
    def __init__(self, ticket_id, address, issue_description, reported_date):
        self.ticket_id = ticket_id
        self.address = address
        self.issue_description = issue_description
        self.reported_date = reported_date

    @classmethod
    def from_dict(cls, data):
        return cls(
            data.get("ticket_id"),
            data.get("address"),
            data.get("issue_description"),
            data.get("reported_date")
        )

    def display(self, priority_choice, contractor_choice):
        print(f"Ticket ID: {self.ticket_id}")
        print(f"Address: {self.address}")
        print(f"Priority: {priority_choice}")
        print(f"Contractor: {contractor_choice}")
        print("-" * 20)