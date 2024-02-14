from flask_login import UserMixin
from . import db
from enums import UserRole, UserAccountType, UserGender
from .utils.utc_now import utcnow

class User(db.Model, UserMixin):
  __tablename__ = 'user'

  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  first_name = db.Column(db.String(20), nullable = False)
  last_name = db.Column(db.String(40), nullable = False)
  email = db.Column(db.String(40), nullable = False)
  email_confirmed = db.Column(db.Boolean, nullable = True)
  gender = db.Column(db.Enum(UserGender), nullable = True)
  birth_date = db.Column(db.Date, nullable = True)
  password_hash = db.Column(db.String(60), nullable = True)
  account_type = db.Column(db.Enum(UserAccountType), nullable = False)
  role = db.Column(db.Enum(UserRole), nullable = False)
  creation_date = db.Column(db.DateTime, nullable = False, server_default = utcnow())
  modification_date = db.Column(db.DateTime, nullable = False, server_default = utcnow())
  
  forums = db.relationship('Forum', backref = 'user', lazy = True)
  messages = db.relationship('Message', backref = 'user', lazy = True, cascade = 'all, delete')
  reviews = db.relationship('Review', backref = 'user', lazy = True)
  salts = db.relationship('Salt', backref = 'user', lazy = True, passive_deletes = True)

  #def __init__(self, first_name, last_name, email, gender, password_hash, account_type, role, **kwargs):
  #  super(User, self).__init__(**kwargs)
  #  self.first_name = first_name
  #  self.last_name = last_name
  #  self.email = email
  #  self.gender = gender
  #  self.password_hash = password_hash
  #  self.account_type = account_type
  #  self.role = role
