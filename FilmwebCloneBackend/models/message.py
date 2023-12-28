from . import db
from .utils.entity import Entity

class Message(db.Model, Entity):
  text = db.Column(db.String(500), nullable=False)
