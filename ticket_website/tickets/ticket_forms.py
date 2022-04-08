from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import DataRequired


# A form used when a user wants to create a new ticket
class CreateTicket(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    contact_number = IntegerField('Contact Number', validators=[DataRequired()])
    affected_item = StringField('Affected Item', validators=[DataRequired()])


# The form used when a user wants to edit a ticket they have created
class EditTicket(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    contact_number = IntegerField('Contact Number', validators=[DataRequired()])
    affected_item = StringField('Affected Item', validators=[DataRequired()])
