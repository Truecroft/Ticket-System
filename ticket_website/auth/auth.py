from flask import Blueprint, flash, render_template, request, redirect, url_for
from .auth_forms import SignupForm, LoginForm
from ticket_website.models import User
from ticket_website import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user


auth = Blueprint('auth', __name__)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists, please login', category='error')
            return redirect(url_for('auth.login'))

        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')

        elif password != confirm_password:
            flash('Passwords Must match', category='error')

        else:
            is_admin = False
            hashed_password = generate_password_hash(password, method='sha256')

            new_user = User(email=email,
             password=hashed_password,
             first_name=first_name,
             last_name=last_name,
             is_admin=is_admin)

            db.session.add(new_user)
            db.session.commit()
            flash('Account Created', category='success')
            login_user(new_user)
            return redirect(url_for('routes.home'))
    return render_template("signup.html", form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        email = request.form.get('email')
        password = request.form.get('password')
        remember_me = request.form.get('remember_me')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                login_user(user, remember=remember_me)
                return redirect(url_for('routes.home'))
            else:
                flash('Incorrect Password, try again', category='error')
        else:
            flash('User does not exist, please signup', category='error')
            return redirect(url_for('auth.signup'))
    return render_template("login.html", form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
