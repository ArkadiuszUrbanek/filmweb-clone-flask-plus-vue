from . import db
from .utils.utc_now import utcnow

class Salt(db.Model):
  __tablename__ = 'salt'

  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  value = db.Column(db.String(32), nullable = False)
  valid = db.Column(db.Boolean, nullable = False)
  creation_date = db.Column(db.DateTime, nullable = False, server_default = utcnow())
  modification_date = db.Column(db.DateTime, nullable = False, server_default = utcnow())

  user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete = 'CASCADE'), nullable = False)