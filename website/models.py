from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    #key that is unique and use
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150) unique=True)
    username = db.Column(db.String(150) unique=True)
    date_created = db.DateTime(db.String(timezone=True) default=func.now())
