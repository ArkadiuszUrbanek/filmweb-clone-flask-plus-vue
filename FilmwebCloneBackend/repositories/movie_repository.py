import datetime
from models import db, Movie

class MovieRepository():

  def findAll(self):
    return Movie.query.order_by(Movie.title).all()
