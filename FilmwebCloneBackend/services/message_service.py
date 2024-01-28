from blueprints import MessageMappers
from dtos import CreateMessageDto
from repositories import MessageRepository


class MessageService():

  messageRepository = MessageRepository()
  messageMappers = MessageMappers()

  def get(self, id):
    dbMessage = self.messageRepository.get(id)
    return self.messageMappers.messageSqlAlchemyToDtoMapper(dbMessage).to_dict()

  def getAllAnswers(self, id):
    answerMessages =  []
    dbMessages = self.messageRepository.getAllAnswers(id)
    convert = lambda unit : self.messageMappers.messageSqlAlchemyToDtoMapper(unit).to_dict()
    for record in dbMessages:
      answerMessages.append(convert(record))
    return answerMessages

  def create(self, forumId, messageDto: CreateMessageDto):
    messageDb = self.messageMappers.createMessageDtoToSqlAlchemyMapper(messageDto)
    return self.messageMappers.messageSqlAlchemyToDtoMapper(self.messageRepository.create(forumId, messageDb)).to_dict()

  def createAnswer(self, parentId, messageDto: CreateMessageDto):
    messageDb = self.messageMappers.createMessageDtoToSqlAlchemyMapper(messageDto)
    return self.messageMappers.messageSqlAlchemyToDtoMapper(self.messageRepository.createAnswer(parentId, messageDb)).to_dict()

  def update(self, id, messageDto: CreateMessageDto):
    messageDb = self.messageMappers.createMessageDtoToSqlAlchemyMapper(messageDto)
    return self.messageMappers.messageSqlAlchemyToDtoMapper(self.messageRepository.update(id, messageDb)).to_dict()

  def delete(self, id):
    messageDb = self.messageRepository.get(id)
    self.messageRepository.delete(messageDb)
    return