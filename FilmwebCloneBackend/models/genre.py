from . import db
from .utils.utc_now import utcnow

class Genre(db.Model):
  __tablename__ = "genre"

  id = db.Column(db.Integer, primary_key = True, autoincrement=True)
  name = db.Column(db.String(100), nullable = False)
  creation_date = db.Column(db.DateTime, nullable = False, server_default = utcnow())
  modification_date = db.Column(db.DateTime, nullable = False, server_default = utcnow())