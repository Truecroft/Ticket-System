from ticket_website import db
from flask_login import UserMixin


# The user model. This is the model which will be created in the database as the users table
class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(255))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    is_admin = db.Column(db.Boolean)

    def is_active(self):
        return super().is_active


# The tickets model. This is the model which will be created in the database as the tickets table
class Ticket(db.Model):
    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000))
    description = db.Column(db.String(10000))
    created_by_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    assigned_to_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    contact_number = db.Column(db.String(150))
    affected_item = db.Column(db.String(1000))
    status = db.Column(db.String(150))

    created_by = db.relationship('User', foreign_keys="Ticket.created_by_id")
    assigned_to = db.relationship('User', foreign_keys="Ticket.assigned_to_id")
