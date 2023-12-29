from . import db
from flask_login import UserMixin
from .utils import utcnow

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(20), nullable = False)
    last_name = db.Column(db.String(40), nullable = False)
    email = db.Column(db.String(40), nullable = False)
    password_hash = db.Column(db.String, nullable = False)
    account_type = db.Column(db.String(8), db.CheckConstraint('account_type IN (\'app\', \'facebook\', \'google\')'), nullable = False)
    role = db.Column(db.String(5), db.CheckConstraint('role IN (\'guest\', \'user\', \'admin\')'), nullable = False)
    creation_date = db.Column(db.DateTime, nullable = False, server_default = utcnow())
