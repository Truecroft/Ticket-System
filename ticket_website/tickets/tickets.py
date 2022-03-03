from flask import Blueprint, flash, render_template, request, redirect, url_for
from flask_login import current_user, login_required

from .ticket_helper import create_new_ticket, edit_ticket_info, populate_edit_ticket_form, update_ticket_status
from .ticket_forms import CreateTicket, EditTicket
from ticket_website.models import Ticket

tickets = Blueprint('tickets', __name__)

@tickets.route('/create-ticket', methods=['GET', 'POST'])
@login_required
def create_ticket():
    form = CreateTicket(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        user_id = current_user.get_id()
        create_new_ticket(request.form, user_id)

        flash('Ticket Created', category='success')
        return redirect(url_for('routes.home'))

    return render_template('create_ticket.html', form=form)


@tickets.route('/view-tickets/<status>', methods=['GET', 'POST'])
@login_required
def view_tickets(status):
    if status == 'open':
        tickets = Ticket.query.filter_by(created_by_id=current_user.get_id(), status="Open").all()
    else:
        tickets = Ticket.query.filter_by(created_by_id=current_user.get_id()).all()
    return render_template("view_tickets.html", tickets=tickets, status=status)


@tickets.route('/edit-ticket/<ticket_id>', methods=['GET', 'POST'])
@login_required
def edit_ticket(ticket_id):
    # test_ticket = Ticket.query.filter_by(id=1).first()
    # print(test_ticket.created_by.first_name)
    form = EditTicket(request.form)
    ticket = Ticket.query.filter_by(id=ticket_id).first()

    if request.method == 'POST' and form.validate_on_submit():
        edit_ticket_info(ticket, request.form)

        flash('Ticket Created', category='success')
        return redirect(url_for('routes.home'))

    populate_edit_ticket_form(form, ticket)
    return render_template("edit_ticket.html", form=form)


@tickets.route('/change-ticket-status/<ticket_id>/<status>')
@login_required
def change_ticket_status(ticket_id, status):
    update_ticket_status(ticket_id, status)

    return redirect(url_for('tickets.view_tickets', status='all'))