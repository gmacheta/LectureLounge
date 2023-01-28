from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import pymongo
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = 'db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "helloworld"
    app.config['SQL_ALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init__app(app)

    from .views import views
    from .auth import auth

    create_datbase(app)

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User


    create_datbase(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    #create session
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

        
    return app


def create_datbase(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print("created")