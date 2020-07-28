import flask
from application import db 
from werkzeug.security import generate_password_hash, check_password_hash


class Users(db.Document):
    name = db.StringField()