from . import db
from .utils.utc_now import utcnow

class Forum(db.Model):
  __tablename__ = "forum"

  id = db.Column(db.Integer, primary_key = True, autoincrement=True)
  name = db.Column(db.String(100), nullable = False)
  description = db.Column(db.String(1000), nullable = True)
  tags = db.Column(db.String(1000), nullable = True)
  creation_date = db.Column(db.DateTime, nullable = False, server_default = utcnow())
  modification_date = db.Column(db.DateTime, nullable = False, server_default = utcnow())

  messages = db.relationship('Message', backref = 'forum', lazy=True, cascade = 'all, delete')
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
  movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)