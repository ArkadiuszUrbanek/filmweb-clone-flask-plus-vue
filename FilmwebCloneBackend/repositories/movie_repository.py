import datetime
from models import db, Movie

class MovieRepository():

  def findAll(self):
    return Movie.query.order_by(Movie.title).all()

  def get(self, id):
    return Movie.query.get(id)

  def create(self, movie):
    movie.creation_date = datetime.datetime.utcnow()
    movie.modification_date = datetime.datetime.utcnow()
    db.session.add(movie)
    db.session.commit()
    return movie

  def update(self, id, movie):
    dbMovie = self.get(id)
    dbMovie.title = movie.title
    dbMovie.premiere_date = movie.premiere_date
    dbMovie.length_time = movie.length_time
    dbMovie.file_path = movie.file_path
    dbMovie.description = movie.description
    dbMovie.directors = movie.directors
    dbMovie.actors = movie.actors
    dbMovie.genres = movie.genres
    dbMovie.forums = movie.forums
    dbMovie.reviews = movie.reviews
    dbMovie.modification_date = datetime.datetime.utcnow()
    db.session.commit()
    return dbMovie

  def delete(self, movie):
    db.session.delete(movie)
    db.session.commit()
    return



