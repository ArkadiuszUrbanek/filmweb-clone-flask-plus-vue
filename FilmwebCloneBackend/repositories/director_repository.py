import datetime
from models import db, Director

class DirectorRepository():

  def findAll(self):
    return Director.query.order_by(Director.last_name).all()

  def get(self, id):
    return Director.query.get(id)

  def create(self, director):
    director.create_date = datetime.datetime.utcnow()
    director.modification_date = datetime.datetime.utcnow()
    db.session.add(director)
    db.session.commit()
    return director

  def update(self, id, director):
    dbDirector = self.get(id)
    dbDirector.first_name = director.first_name
    dbDirector.last_name = director.last_name
    dbDirector.nationality = director.nationality
    dbDirector.file_path = director.file_path
    dbDirector.description = director.description
    dbDirector.modification_date = datetime.datetime.utcnow()
    db.session.commit()
    return dbDirector

  def delete(self, director):
    db.session.delete(director)
    db.session.commit()
    return