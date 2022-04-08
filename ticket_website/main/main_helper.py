from ticket_website.models import Ticket


# A helper to create a dictionary to display the amount of tickets with different status'
def ticket_count_dict_helper(user_id):
    ticket_count_dict = {
        "Open": 0,
        "In Progress": 0,
        "Resolved": 0,
        "Closed": 0
    }

    tickets = Ticket.query.filter_by(created_by_id=user_id)
    for ticket in tickets:
        ticket_count_dict[ticket.status] += 1

    return ticket_count_dict
