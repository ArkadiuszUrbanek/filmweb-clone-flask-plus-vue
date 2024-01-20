import datetime
from models import db, Genre

class GenreRepository():

 def findAll(self):
  return Genre.query.order_by(Genre.name).all()

 def get(self, id):
  return Genre.query.get(id)

 def create(self, genre):
  genre.create_date = datetime.datetime.utcnow()
  genre.modification_date = datetime.datetime.utcnow()
  db.session.add(genre)
  db.session.commit()
  return genre

 def update(self, id, genre):
  dbGenre = self.get(id)
  dbGenre.name = genre.name
  dbGenre.modification_date = datetime.datetime.utcnow()
  db.session.commit()
  return dbGenre

 def delete(self, genre):
  db.session.delete(genre)
  db.session.commit()
  return
