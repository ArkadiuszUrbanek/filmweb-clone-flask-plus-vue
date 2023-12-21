from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(20), nullable = False)
    last_name = db.Column(db.String(40), nullable = False)
    email = db.Column(db.String(40), nullable = False)
    account_type = db.Column(db.String(8), nullable = False)
    creation_date = db.Column(db.Date, nullable = False)