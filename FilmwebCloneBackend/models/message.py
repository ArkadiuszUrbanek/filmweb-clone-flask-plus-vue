from . import db
from .blueprints.entity import Entity

class Message(db.Model, Entity):
  text = db.Column(db.String(500), nullable = False)

  forum = db.relationship('Forum', back_populates = 'messages')
  author = db.relationship('User', back_populates = 'messages')
  main_message_id = db.Column(db.Integer, db.ForeignKey('message.id'), nullable = True)
  main_message = db.relationship('Message', backref = 'main_message', remote_side='message.id', cascade = 'all, delete')