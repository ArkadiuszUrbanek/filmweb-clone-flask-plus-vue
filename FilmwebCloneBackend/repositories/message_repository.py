import datetime
from models import db, Message

class MessageRepository():

  def get(self, id):
    return Message.query.get(id)

  def getAllAnswers(self, id):
    #return Message.query.get(id).messages.order_by(Message.messages.creation_date)
    return Message.query.get(id).options(db.load_only('messages')).order_by(Message.messages.creation_date).all()

  def create(self, message):
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
    answers = parentMessage.messages
    answers.append(message)
    parentMessage.messages = answers
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