from . import db
from enums import UserGender
from .blueprints.artist import Artist
from .utils.utc_now import utcnow

class Actor(db.Model, Artist):
  __tablename__ = 'actor'

  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  creation_date = db.Column(db.DateTime, nullable = False, server_default = utcnow())
  modification_date = db.Column(db.DateTime, nullable = False, server_default = utcnow())

  def __init__(self, first_name, last_name, nationality, file_path, description, gender, height, birth_date, **kwargs):
    super(Actor, self).__init__(**kwargs)
    self.first_name = first_name
    self.last_name = last_name
    self.nationality = nationality
    self.file_path = file_path
    self.description = description
    self.gender = gender
    self.height = height
    self.birth_date = birth_date