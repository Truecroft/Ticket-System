from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo


# A form to be used for the login page
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Email Address"})
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')


# A form to be used for a user to signup to the system
class SignupForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "john@doe.com"})
    first_name = StringField('First Name', validators=[DataRequired()], render_kw={"placeholder": "John"})
    last_name = StringField('Last Name', validators=[DataRequired()], render_kw={"placeholder": "Doe"})
    password = PasswordField('Password',
        validators=[DataRequired()], render_kw={"placeholder": "Password"})
    confirm_password = PasswordField('Confirm Password',
        validators=[DataRequired(), EqualTo('confirm_password', message='Passwords Must Match')],
        render_kw={"placeholder": "Confirm Password"})
    remember_me = BooleanField('Remember Me')
