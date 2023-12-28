from . import db
from .utils.entity import Entity

class Forum(db.Model, Entity):
  name = db.Column(db.String(100), nullable = False)
  description = db.Column(db.String(1000), nullable = True)
  tags = db.Column(db.String(1000), nullable = True)