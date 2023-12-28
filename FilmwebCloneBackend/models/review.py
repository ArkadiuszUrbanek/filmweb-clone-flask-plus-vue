from . import db
from .utils.entity import Entity

class Review(db.Model, Entity):
  mark = db.Column(db.Integer, nullable = False)
  description = db.Column(db.String(500), nullable = True)
