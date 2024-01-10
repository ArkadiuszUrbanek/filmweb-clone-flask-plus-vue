import datetime
from models import db, Message

class MessageRepository():

  def get(self, id):
    return Message.query.get(id)

  def getAllAnswers(self, id):
    return Message.query.filter_by(main_message = id).order_by(Message.id).all()

  def create(self, forumId, message):
    message.forum_id = forumId
    message.creation_date = datetime.datetime.utcnow()
    message.modification_date = datetime.datetime.utcnow()
    db.session.add(message)
    db.session.commit()
    return message

  def createAnswer(self, parentId, message):
    parentMessage = self.get(parentId)
    message.forum_id = parentMessage.forum_id
    message.main_message = parentMessage.id
    message.creation_date = datetime.datetime.utcnow()
    message.modification_date = datetime.datetime.utcnow()
    db.session.add(message)
    db.session.commit()
    return message

  def update(self, id, message):
    dbMessage = self.get(id)
    dbMessage.text = message.text
    dbMessage.modification_date = datetime.datetime.utcnow()
    db.session.commit()
    return dbMessage

  def delete(self, message):
    db.session.delete(message)
    db.session.commit()
    return