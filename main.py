import json

from defineticket import MaintenanceTicket
from decision import priority_choice, contractor_choice


def load_ticket(file_name):
    with open(file_name) as file:
        info = json.load(file)

    tickets = []

    for item in info:
        ticket = MaintenanceTicket(
            item.get("ticket_id"),
            item.get("address"),
            item.get("issue_description"),
            item.get("reported_date")
        )

        tickets.append(ticket)

    return tickets

def display_results(tickets):

    for ticket in tickets:
        priority = priority_choice(ticket.issue_description)
        contractor = contractor_choice(ticket.issue_description)

        print(f"Ticket ID: {ticket.ticket_id}")
        print(f"Address: {ticket.address}")
        print(f"Priority: {priority}")
        print(f"Contractor: {contractor}")
        print("-" * 20)

def main():
    tickets = load_ticket("tickets.json")
    display_results(tickets)


if __name__ == "__main__":
    main()
