import json

from maintenance_ticket import MaintenanceTicket
from decision import priority_choice, contractor_choice


def load_ticket(file_name):
    with open(file_name) as file:
        info = json.load(file)

    tickets = []

    for item in info:
        ticket = MaintenanceTicket.from_dict(item)
        tickets.append(ticket)

    return tickets

def display_results(tickets):

    for ticket in tickets:
        priority = priority_choice(ticket.issue_description)
        contractor = contractor_choice(ticket.issue_description)

        ticket.display(priority, contractor)

def main():
    tickets = load_ticket("tickets.json")
    display_results(tickets)


if __name__ == "__main__":
    main()