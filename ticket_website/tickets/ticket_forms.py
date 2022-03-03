from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class CreateTicket(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    contact_number = IntegerField('Contact Number', validators=[DataRequired()])
    affected_item = StringField('Affected Item', validators=[DataRequired()])
    # status = SelectField('Programming Language', choices=[('open', 'Open'), ('resolved', 'Resolved'), ('closed', 'Closed')])

class EditTicket(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    contact_number = IntegerField('Contact Number', validators=[DataRequired()])
    affected_item = StringField('Affected Item', validators=[DataRequired()])
    # status = SelectField('Programming Language', choices=[('open', 'Open'), ('resolved', 'Resolved'), ('closed', 'Closed')])