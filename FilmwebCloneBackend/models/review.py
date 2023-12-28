from . import db
from .utils.entity import Entity

class Review(db.Model, Entity):
  mark = db.Column(db.Integer, nullable = False)
  description = db.Column(db.String(500), nullable = True)

  user = db.relationship("User", back_populates="review")

  movie = db.relationship("Movie", back_populates="review")