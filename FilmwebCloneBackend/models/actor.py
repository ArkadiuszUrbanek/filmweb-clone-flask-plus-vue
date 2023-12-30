from .blueprints import db
from .movie_actor import movie_actor
from .blueprints.artist import Artist

class Actor(db.Model, Artist):
  movies = db.relationship('Movie', secondary = movie_actor, back_populates = 'actors')