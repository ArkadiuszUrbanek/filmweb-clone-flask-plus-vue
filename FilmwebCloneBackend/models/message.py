from . import db
from .utils.entity import Entity

class Message(db.Model, Entity):
  text = db.Column(db.String(500), nullable=False)

  forum = db.relationship("Forum", back_populates="message", cascade = "all, delete")

  author = db.relationship("User", back_populates="message")

  main_message = db.relationship("Message", back_populates="message", cascade = "all, delete")
  answer_message_id = db.Column(db.Integer, db.ForeignKey("message.id"), nullable=True)
  answer_messages = db.relationship("Message", back_populates="message")