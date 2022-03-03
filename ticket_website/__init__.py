from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from os import path

db = SQLAlchemy()
DB_NAME = "ticket_database.db"

def create_app():
    app = Flask(__name__)
    Bootstrap(app)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    db.init_app(app)

    from ticket_website.main.routes import routes
    from ticket_website.auth.auth import auth
    from ticket_website.tickets.tickets import tickets
    from ticket_website.admin.admin import admin

    app.register_blueprint(routes, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(tickets, url_prefix='/')
    app.register_blueprint(admin, url_prefix='/')
    
    from ticket_website.models import User, Ticket

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('ticket_website' + DB_NAME):
        db.create_all(app=app)
        print("Created Database")