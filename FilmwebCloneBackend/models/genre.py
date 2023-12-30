from . import db
from .movie_genre import movie_genre
from .blueprints.entity import Entity

class Genre(db.Model, Entity):
  name = db.Column(db.String(100), nullable = False)

  movies = db.relationship('Movie', secondary = movie_genre, back_populates = 'genres')