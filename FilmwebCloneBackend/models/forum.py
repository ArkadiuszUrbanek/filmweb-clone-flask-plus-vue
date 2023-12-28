from . import db
from .utils.entity import Entity

class Forum(db.Model, Entity):
  name = db.Column(db.String(100), nullable = False)
  description = db.Column(db.String(1000), nullable = True)
  tags = db.Column(db.String(1000), nullable = True)

  message_id = db.Column(db.Integer, db.ForeignKey("message.id"), nullable=True)
  messages = db.relationship("Message", back_populates="forum")

  author = db.relationship("User", back_populates="forum")

  movie = db.relationship("Movie", back_populates="forum")