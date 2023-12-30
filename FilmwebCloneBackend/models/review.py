from . import db
from .blueprints.entity import Entity

class Review(db.Model, Entity):
  mark = db.Column(db.Integer, nullable = False)
  description = db.Column(db.String(500), nullable = True)

  author = db.relationship('User', back_populates = 'reviews')
  movie = db.relationship('Movie', back_populates = 'reviews')