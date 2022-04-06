from flask_wtf import FlaskForm
from sqlalchemy import false, true
from wtforms import StringField, IntegerField, TextAreaField, PasswordField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo

class CreateUser(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "john@doe.com"})
    first_name = StringField('First Name', validators=[DataRequired()], render_kw={"placeholder": "John"})
    last_name = StringField('Last Name', validators=[DataRequired()], render_kw={"placeholder": "Doe"})
    password = PasswordField('Password', validators=[DataRequired()],render_kw={"placeholder": "Password"})

    confirm_password = PasswordField('Confirm Password', 
        validators=[DataRequired(), EqualTo('confirm_password', message='Passwords Must Match')], 
        render_kw={"placeholder": "Confirm Password"})
    
    user_status = SelectField('Is this User an Admin', choices=[('admin', 'Admin User'), ('regular', 'Regular User')], validate=False)


class EditTicket(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    contact_number = IntegerField('Contact Number', validators=[DataRequired()])
    affected_item = StringField('Affected Item', validators=[DataRequired()])
    status = SelectField('Status', 
        choices=[('Open', 'Open'), ('In Progress', 'In Progress'), ('Resolved', 'Resolved'), ('Closed', 'Closed')])


class EditUser(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "john@doe.com"})
    first_name = StringField('First Name', validators=[DataRequired()], render_kw={"placeholder": "John"})
    last_name = StringField('Last Name', validators=[DataRequired()], render_kw={"placeholder": "Doe"})    
    user_status = SelectField('Is this User an Admin', choices=[('admin', 'Admin User'), ('regular', 'Regular User')], validate=False)