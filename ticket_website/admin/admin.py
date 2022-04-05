from flask import Blueprint, flash, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from .admin_forms import CreateUser, EditTicket, EditUser
from .admin_helper import *
from ticket_website.models import Ticket, User

admin = Blueprint('admin', __name__)

@admin.route('/admin-home', methods=['GET', 'POST'])
@login_required
def admin_home():
    if not current_user.is_admin:
        flash(f"You must be an admin to view that page. Returning to the Home page.", category='error')
        return redirect(url_for('routes.home'))
        
    tickets = Ticket.query.filter_by(created_by_id=current_user.get_id(), status="Open").all()
    return render_template('admin/admin_home.html', tickets=tickets)


@admin.route('/create-new-user', methods=['GET', 'POST'])
@login_required
def create_new_user():
    if not current_user.is_admin:
        flash(f"You must be an admin to view that page. Returning to the Home page.", category='error')
        return redirect(url_for('routes.home'))

    form = CreateUser(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        create_new_user_helper(request.form)
        return redirect(url_for('admin.admin_home'))
    return render_template('admin/create_new_user.html', form=form)


@admin.route('/view-regular-users', methods=['GET'])
@login_required
def view_regular_users():
    if not current_user.is_admin:
        flash(f"You must be an admin to view that page. Returning to the Home page.", category='error')
        return redirect(url_for('routes.home'))

    users = User.query.filter_by(is_admin=False).all()

    return render_template('admin/view_regular_users.html', users=users)


@admin.route('/edit_user/<user_id>', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    if not current_user.is_admin:
        flash(f"You must be an admin to view that page. Returning to the Home page.", category='error')
        return redirect(url_for('routes.home'))

    form = EditUser(request.form)
    user = User.query.filter_by(id=user_id).first()
    if request.method == 'POST' and form.validate_on_submit():
        edit_user_info(user, request.form)

        flash('User Updated', category='success')
        return redirect(url_for('admin.admin_home'))

    populate_edit_user_form(form, user)
    return render_template('admin/edit_user.html', form=form)


@admin.route('/delete-user/<user_id>', methods=['GET'])
@login_required
def delete_user(user_id):
    if not current_user.is_admin:
        flash(f"You must be an admin to view that page. Returning to the Home page.", category='error')
        return redirect(url_for('routes.home'))

    delete_user_helper(user_id)
    flash('User Deleted', category='success')
    return redirect(url_for('admin.admin_home'))


@admin.route('/view-admin-users', methods=['GET'])
@login_required
def view_admin_users():
    if not current_user.is_admin:
        flash(f"You must be an admin to view that page. Returning to the Home page.", category='error')
        return redirect(url_for('routes.home'))

    users = User.query.filter_by(is_admin=True).all()
    return render_template('admin/view_admin_users.html', users=users)


@admin.route('/view-admin-tickets/<status>', methods=['GET', 'POST'])
@login_required
def view_admin_tickets(status):
    if not current_user.is_admin:
        flash(f"You must be an admin to view that page. Returning to the Home page.", category='error')
        return redirect(url_for('routes.home'))

    if status == 'all':
        tickets = Ticket.query.all()
        if len(tickets) < 1:
            flash(f"There are no tickets available. Returning to the Home page.", category='error')
            return redirect(url_for('admin.admin_home'))
    else:
        tickets = Ticket.query.filter_by(status=status).all()

    if len(tickets) < 1:
        flash(f"There are no tickets with status: {status}.", category='error')
        return redirect(url_for('admin.view_admin_tickets', status='all'))

    return render_template('admin/admin_view_tickets.html', tickets=tickets, status=status)


@admin.route('/view-assigned-tickets', methods=['GET', 'POST'])
@login_required
def view_assigned_tickets():
    if not current_user.is_admin:
        flash(f"You must be an admin to view that page. Returning to the Home page.", category='error')
        return redirect(url_for('routes.home'))

    tickets = Ticket.query.filter_by(assigned_to_id=current_user.get_id()).all()

    if len(tickets) < 1:
        flash(f"You currently have no tickets assigned to yourself. Returning to Home Page", category='error')
        return redirect(url_for('admin.admin_home'))

    return render_template('admin/admin_view_tickets.html', tickets=tickets)


@admin.route('/delete-ticket/<ticket_id>', methods=['GET', 'POST'])
@login_required
def delete_ticket(ticket_id):
    if not current_user.is_admin:
        flash(f"You must be an admin to view that page. Returning to the Home page.", category='error')
        return redirect(url_for('routes.home'))

    delete_ticket_helper(ticket_id)
    return redirect(url_for('admin.view_admin_tickets', status='all'))


@admin.route('/assign-ticket/<ticket_id>', methods=['GET', 'POST'])
@login_required
def assign_ticket(ticket_id):
    if not current_user.is_admin:
        flash(f"You must be an admin to view that page. Returning to the Home page.", category='error')
        return redirect(url_for('routes.home'))

    assign_ticket_helper(ticket_id)
    flash(f"Ticket assigned to {current_user.first_name}", category='success')
    return redirect(url_for('admin.view_admin_tickets', status='all'))


@admin.route('/unassign-ticket/<ticket_id>', methods=['GET', 'POST'])
@login_required
def unassign_ticket(ticket_id):
    if not current_user.is_admin:
        flash(f"You must be an admin to view that page. Returning to the Home page.", category='error')
        return redirect(url_for('routes.home'))

    unassign_ticket_helper(ticket_id)
    flash(f"Ticket unassigned from {current_user.first_name}", category='success')
    return redirect(url_for('admin.view_admin_tickets', status='all'))


@admin.route('/edit-ticket-admin/<ticket_id>', methods=['GET', 'POST'])
@login_required
def edit_ticket_admin(ticket_id):
    if not current_user.is_admin:
        flash(f"You must be an admin to view that page. Returning to the Home page.", category='error')
        return redirect(url_for('routes.home'))
         
    form = EditTicket(request.form)
    ticket = Ticket.query.filter_by(id=ticket_id).first()

    if request.method == 'POST' and form.validate_on_submit():
        edit_ticket_info(ticket, request.form)

        flash('Ticket Updated', category='success')
        return redirect(url_for('admin.view_admin_tickets', status='all'))

    populate_edit_ticket_form(form, ticket)
    return render_template("admin/edit_ticket_admin.html", form=form)