from . import db
from .movie_actor import movie_actor
from .movie_director import movie_director
from .movie_genre import movie_genre
from .entity import Entity
from .utils.utc_now import utcnow

class Movie(db.Model, Entity):
  title = db.Column(db.String(100), nullable = False)
  premiere_date = db.Column(db.DateTime, nullable = True, server_default = utcnow())
  length_time = db.Column(db.Integer, nullable = True)
  description = db.Column(db.String(10000), nullable = True)

  review_id = db.Column(db.Integer, db.ForeignKey('review.id'), nullable = True)
  reviews = db.relationship('Review', back_populates = 'movie',  cascade = 'all, delete')
  forum_id = db.Column(db.Integer, db.ForeignKey("forum.id"), nullable = True)
  forums = db.relationship('Forum', back_populates = 'movie', cascade = 'all, delete')
  directors = db.relationship('Director', secondary = movie_director, back_populates = 'movies')
  actors = db.relationship('Actor', secondary = movie_actor, back_populates = 'movies')
  genres = db.relationship('Genre', secondary = movie_genre, back_populates = 'movies')