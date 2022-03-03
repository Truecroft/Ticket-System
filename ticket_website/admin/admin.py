from flask import Blueprint, flash, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from .admin_forms import CreateUser

from ticket_website.models import Ticket

admin = Blueprint('admin', __name__)

@admin.route('/create-new-user', methods=['GET', 'POST'])
def create_new_user():
    form = CreateUser(request.form)
    return render_template('create_ticket.html', form=form)