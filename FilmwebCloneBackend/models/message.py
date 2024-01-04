from . import db
from .utils.utc_now import utcnow

class Message(db.Model):
  __tablename__ = 'message'

  id = db.Column(db.Integer, primary_key = True, autoincrement=True)
  text = db.Column(db.String(500), nullable = False)
  creation_date = db.Column(db.DateTime, nullable = False, server_default = utcnow())
  modification_date = db.Column(db.DateTime, nullable = False, server_default = utcnow())

  forum_id = db.Column(db.Integer, db.ForeignKey('forum.id'), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  main_message = db.Column(db.Integer, db.ForeignKey('message.id'), nullable = True)
  messages= db.relationship('Message', backref = db.backref('parent', lazy='subquery'), remote_side=id, cascade = 'all, delete')