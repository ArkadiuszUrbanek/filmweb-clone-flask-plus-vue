from flask_login import UserMixin
from . import db
from .blueprints.entity import Entity
from enums import UserRole, UserAccountType

class User(db.Model, Entity, UserMixin):
  first_name = db.Column(db.String(20), nullable = False)
  last_name = db.Column(db.String(40), nullable = False)
  email = db.Column(db.String(40), nullable = False)
  password_hash = db.Column(db.String(50), nullable = False)
  account_type = db.Column(db.Enum(UserAccountType), nullable = False)
  role = db.Column(db.Enum(UserRole), nullable = False)

  forum_id = db.Column(db.Integer, db.ForeignKey('forum.id'), nullable = True)
  forums = db.relationship('Forum', back_populates = 'author', lazy=True, cascade = 'all, delete')
  message_id = db.Column(db.Integer, db.ForeignKey('message.id'), nullable = True)
  messages = db.relationship('Message', back_populates = 'author', lazy=True, cascade = 'all, delete')
  review_id = db.Column(db.Integer, db.ForeignKey('review.id'), nullable = True)
  reviews = db.relationship('Review', back_populates = 'author', lazy=True)

  def __init__(self, first_name, last_name, email, password_hash, account_type, role, **kwargs):
    super(User, self).__init__(**kwargs)
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.password_hash = password_hash
    self.account_type = account_type
    self.role = role
