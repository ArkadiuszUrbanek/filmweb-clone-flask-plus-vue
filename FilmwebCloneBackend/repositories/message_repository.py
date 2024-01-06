import datetime
from models import db
from models.message import Message

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

  def createAnswer(self, parentId, answer):
    parentMessage = self.get(parentId)
    answers = parentMessage.messages
    answers.append(answer)
    parentMessage.messages = answers
    answer.main_message = parentId
    answer.creation_date = datetime.datetime.utcnow()
    answer.modification_date = datetime.datetime.utcnow()
    db.session.commit()
    return answer

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