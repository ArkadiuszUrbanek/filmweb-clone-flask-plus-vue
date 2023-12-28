from . import db
from .utils.entity import Entity

class Genre(db.Model, Entity):
  name = db.Column(db.String(100), nullable = False)