from . import db
from .movie_actor import movie_actor
from .movie_director import movie_director
from .movie_genre import movie_genre
from .utils.utc_now import utcnow

class Movie(db.Model):
  __tablename__ = 'movie'

  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  title = db.Column(db.String(100), nullable = False)
  subtitle = db.Column(db.String(500), nullable = False)
  premiere_date = db.Column(db.DateTime, nullable = True, server_default = utcnow())
  length_time = db.Column(db.Integer, nullable = True)
  file_path = db.Column(db.String(500), nullable = True)
  description = db.Column(db.String(10000), nullable = True)
  creation_date = db.Column(db.DateTime, nullable = False, server_default = utcnow())
  modification_date = db.Column(db.DateTime, nullable = False, server_default = utcnow())

  reviews = db.relationship('Review', backref = 'movie',  cascade = 'all, delete')
  forums = db.relationship('Forum', backref = 'movie')
  directors = db.relationship('Director', secondary = movie_director, lazy = 'subquery', backref = db.backref('movies', lazy = 'subquery'))
  actors = db.relationship('Actor', secondary = movie_actor, lazy = 'subquery', backref = db.backref('movies', lazy = 'subquery'))
  genres = db.relationship('Genre', secondary = movie_genre, lazy = 'subquery', backref = db.backref('movies', lazy = 'subquery'))

  def __init__(self, title, subtitle, premiere_date, length_time, file_path, description, **kwargs):
    super(Movie, self).__init__(**kwargs)
    self.title = title
    self.subtitle = subtitle
    self.premiere_date = premiere_date
    self.length_time = length_time
    self.file_path = file_path
    self.description = description
