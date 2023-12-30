from . import db
from .entity import Entity

class Message(db.Model, Entity):
  text = db.Column(db.String(500), nullable = False)

  forum = db.relationship('Forum', back_populates = 'messages')
  author = db.relationship('User', back_populates = 'messages')
  main_message = db.relationship('Message', back_populates = 'answer_messages', cascade = 'all, delete')
  answer_message_id = db.Column(db.Integer, db.ForeignKey('message.id'), nullable = True)
  answer_messages = db.relationship('Message', back_populates = 'main_message')