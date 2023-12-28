from Models import db
from .utcnow import utcnow

class Entity(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  creation_date = db.Column(db.DateTime, nullable = False, server_default = utcnow())
  modification_date = db.Column(db.DateTime, nullable = False, server_default = utcnow())