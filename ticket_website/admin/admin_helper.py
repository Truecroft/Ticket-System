from flask import flash, redirect, url_for
from flask_login import current_user
from ticket_website import db
from ticket_website.models import Ticket, User
from werkzeug.security import generate_password_hash


def delete_ticket_helper(ticket_id):
    Ticket.query.filter_by(id=ticket_id).delete()
    db.session.commit()


def assign_ticket_helper(ticket_id):
    ticket = Ticket.query.filter_by(id=ticket_id).first()
    ticket.assigned_to_id = current_user.get_id()
    db.session.commit()


def unassign_ticket_helper(ticket_id):
    ticket = Ticket.query.filter_by(id=ticket_id).first()
    ticket.assigned_to_id = -1
    db.session.commit()


def populate_edit_ticket_form(form, ticket_data):
    form.title.data = ticket_data.title
    form.description.data = ticket_data.description
    form.contact_number.data = ticket_data.contact_number
    form.affected_item.data = ticket_data.affected_item
    form.status = ticket_data.status
    return form


def edit_ticket_info(ticket, form):
    ticket.title = form.get('title')
    ticket.description = form.get('description')
    ticket.contact_number = form.get('contact_number')
    ticket.affected_item = form.get('affected_item')
    ticket.status = form.get('status')

    db.session.commit()


def create_new_user_helper(form_data):
    email = form_data.get('email')
    first_name = form_data.get('first_name')
    last_name = form_data.get('last_name')
    password = form_data.get('password')
    confirm_password = form_data.get('confirm_password')
    user_status = form_data.get('user_status')

    user = User.query.filter_by(email=email).first()
    if user:
        flash('Email already exists', category='error')
        return redirect(url_for('admin.admin_home'))

    elif len(email) < 4:
        flash('Email must be greater than 4 characters.', category='error')

    elif password != confirm_password:
        flash('Passwords Must match', category='error')

    else:
        hashed_password = generate_password_hash(password, method='sha256')
        if user_status == "True":
            is_admin = True
        else:
            is_admin = False

        new_user = User(email=email,
            password=hashed_password,
            first_name=first_name,
            last_name=last_name,
            is_admin=is_admin)

        db.session.add(new_user)
        db.session.commit()
        flash('Account Created', category='success')


def populate_edit_user_form(form, user_data):
    form.first_name.data = user_data.first_name
    form.last_name.data = user_data.last_name
    form.email.data = user_data.email
    return form


def edit_user_info(ticket, form):
    ticket.first_name = form.get('first_name')
    ticket.last_name = form.get('last_name')
    ticket.email = form.get('email')
    if form.get('user_status') == "True":
        is_admin = True
    else:
        is_admin = False
    ticket.is_admin = is_admin

    db.session.commit()


def delete_user_helper(user_id):
    User.query.filter_by(id=user_id).delete()
    db.session.commit()
