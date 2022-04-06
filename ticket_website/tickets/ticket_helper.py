from ticket_website import db
from ticket_website.models import Ticket


def populate_edit_ticket_form(form, ticket_data):
    form.title.data = ticket_data.title
    form.description.data = ticket_data.description
    form.contact_number.data = ticket_data.contact_number
    form.affected_item.data = ticket_data.affected_item
    return form


def create_new_ticket(form, user_id):
    title = form.get('title')
    description = form.get('description')
    contact_number = form.get('contact_number')
    affected_item = form.get('affected_item')
    status = "Open"

    new_ticket = Ticket(title=title,
        description=description,
        created_by_id=user_id,
        contact_number=contact_number,
        affected_item=affected_item,
        status=status)
   
    db.session.add(new_ticket)
    db.session.commit()


def edit_ticket_info(ticket, form):
    ticket.title = form.get('title')
    ticket.description = form.get('description')
    ticket.contact_number = form.get('contact_number')
    ticket.affected_item = form.get('affected_item')
    db.session.commit()


def update_ticket_status(ticket_id, status):
    ticket = Ticket.query.filter_by(id=ticket_id).first()
    ticket.status = status
    db.session.commit()
