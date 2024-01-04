from . import db
from .blueprints.artist import Artist
from .utils.utc_now import utcnow

class Director(db.Model, Artist):
  __tablename__ = 'director'

  id = db.Column(db.Integer, primary_key = True, autoincrement=True)
  creation_date = db.Column(db.DateTime, nullable = False, server_default = utcnow())
  modification_date = db.Column(db.DateTime, nullable = False, server_default = utcnow())