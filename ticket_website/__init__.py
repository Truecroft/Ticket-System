from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
import os
from os import path

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    Bootstrap(app)

    app.config['SECRET_KEY'] = os.urandom(24)

    # This DB_URI Section below is to fix a bug within the heroku Database_Url which it returns.
    # SqlAlchemy versions > 1.4 (I am using 2.5.1) requires the database url to be prefixed with
    # postgresql:// instead of postgres://
    # The fix was found from the Heroku website
    # https://help.heroku.com/ZKNTJQSK/why-is-sqlalchemy-1-4-x-not-connecting-to-heroku-postgres

    DB_URI = os.environ.get('DATABASE_URL')
    if DB_URI.startswith("postgres://"):
        DB_URI = DB_URI.replace("postgres://", "postgresql://", 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

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
    def load_user(user_id):
        try:
            return User.query.get(user_id)
        except:
            return None

    return app

def create_database(app):
    db.create_all(app=app)
    print("Created Database")