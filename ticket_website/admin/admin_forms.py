from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, PasswordField, SelectField, RadioField
from wtforms.validators import DataRequired, Email, EqualTo


# This is a form which is used when an admin wants to create a new user
class CreateUser(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "john@doe.com"})
    first_name = StringField('First Name', validators=[DataRequired()], render_kw={"placeholder": "John"})
    last_name = StringField('Last Name', validators=[DataRequired()], render_kw={"placeholder": "Doe"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Password"})

    confirm_password = PasswordField('Confirm Password',
        validators=[DataRequired(), EqualTo('confirm_password', message='Passwords Must Match')],
        render_kw={"placeholder": "Confirm Password"})

    user_status = RadioField('Is this User an Admin', choices=[(True, 'Admin User'), (False, 'Regular User')], default=False)


# This is a form which will be used when an admin wants to edit a ticket
class EditTicket(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    contact_number = IntegerField('Contact Number', validators=[DataRequired()])
    affected_item = StringField('Affected Item', validators=[DataRequired()])
    status = SelectField('Status',
        choices=[('Open', 'Open'), ('In Progress', 'In Progress'), ('Resolved', 'Resolved'), ('Closed', 'Closed')])


# This will be used when an admin wants to edit an exisiting user
class EditUser(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "john@doe.com"})
    first_name = StringField('First Name', validators=[DataRequired()], render_kw={"placeholder": "John"})
    last_name = StringField('Last Name', validators=[DataRequired()], render_kw={"placeholder": "Doe"})
    user_status = RadioField('Is this User an Admin', choices=[(True, 'Admin User'), (False, 'Regular User')], default=False)
