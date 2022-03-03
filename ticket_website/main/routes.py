from flask import Blueprint, render_template
from flask_login import login_required, current_user

from .main_helper import ticket_count_dict_helper

routes = Blueprint('routes', __name__)

@routes.route('/')
@login_required
def home():
    user_id = current_user.get_id()
    ticket_count_dict = ticket_count_dict_helper(user_id)
    print(ticket_count_dict)
    return render_template("home.html", ticket_count_dict=ticket_count_dict)