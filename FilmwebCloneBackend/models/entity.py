from models import db
from .utils import utcnow

class Entity():
  id = db.Column(db.Integer, primary_key = True)
  creation_date = db.Column(db.DateTime, nullable = False, server_default = utcnow())
  modification_date = db.Column(db.DateTime, nullable = False, server_default = utcnow())