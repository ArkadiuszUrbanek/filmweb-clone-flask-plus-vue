from blueprints import MessageMappers
from dtos import CreateMessageDto
from repositories import MessageRepository


class MessageService():

  messageRepository = MessageRepository()
  messageMappers = MessageMappers()

  def get(self, id):
    dbMessage = self.messageRepository.get(id)
    return self.messageMappers.messageSqlAlchemyToDtoMapper(dbMessage)

  def getAllAnswers(self, id):
    answerMessages =  []
    dbMessages = self.messageRepository.getAllAnswers(id)
    convert = lambda unit : self.messageMappers.messageSqlAlchemyToDtoMapper(unit)
    for record in dbMessages:
      answerMessages.append(convert(record))
    return answerMessages

  def create(self, forumId, messageDto: CreateMessageDto):
    messageDb = self.messageMappers.createMessageDtoToSqlAlchemyMapper(messageDto)
    return self.messageRepository.create(forumId, messageDb)

  def createAnswer(self, parentId, messageDto: CreateMessageDto):
    messageDb = self.messageMappers.createMessageDtoToSqlAlchemyMapper(messageDto)
    return self.messageRepository.createAnswer(parentId, messageDb)

  def update(self, id, messageDto: CreateMessageDto):
    messageDb = self.messageMappers.createMessageDtoToSqlAlchemyMapper(messageDto)
    return self.messageRepository.update(id, messageDb)

  def delete(self, id):
    messageDb = self.messageRepository.get(id)
    self.messageRepository.delete(messageDb)
    return