from . import db
from .utils.utc_now import utcnow

class Review(db.Model):
  __tablename__ = "review"

  id = db.Column(db.Integer, primary_key = True, autoincrement=True)
  mark = db.Column(db.Integer, nullable = False)
  description = db.Column(db.String(500), nullable = True)
  creation_date = db.Column(db.DateTime, nullable = False, server_default = utcnow())
  modification_date = db.Column(db.DateTime, nullable = False, server_default = utcnow())

  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
  movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)