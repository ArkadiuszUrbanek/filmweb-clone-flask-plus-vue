from . import db
from .utils.entity import Entity

class Forum(db.Model, Entity):
  name = db.Column(db.String(100), nullable = False)
  description = db.Column(db.String(1000), nullable = True)
  tags = db.Column(db.String(1000), nullable = True)

  message_id = db.Column(db.Integer, db.ForeignKey("message.id"), nullable=True)
  messages = db.relationship("Message", back_populates="forum", cascade = "all, delete")
  author = db.relationship("User", back_populates="forums")
  movie = db.relationship("Movie", back_populates="forums")