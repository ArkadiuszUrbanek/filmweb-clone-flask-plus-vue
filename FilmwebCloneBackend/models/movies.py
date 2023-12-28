from . import db
from .utils.entity import Entity
from .utils.utcnow import utcnow

class Movies(db.Model, Entity):
  title = db.Column(db.String(100), nullable=False)
  premiere_date = db.Column(db.DateTime, nullable=True, server_default = utcnow())
  length_time = db.Column(db.Integer, nullable=True)
  description = db.Column(db.String(10000), nullable=True)