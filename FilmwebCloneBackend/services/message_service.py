from blueprints import MessageMappers
from dtos import MessageDto, CreateMessageDto
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

  def create(self, messageDto: CreateMessageDto):
    messageDb = self.messageMappers.createMessageDtoToSqlAlchemyMapper(messageDto)
    return self.messageRepository.create(messageDb)

  def createAnswer(self, parentId, messageDto: CreateMessageDto):
    messageDb = self.messageMappers.createMessageDtoToSqlAlchemyMapper(messageDto)
    return self.messageRepository.createAnswer(parentId, messageDb)

  def update(self, id, messageDto: CreateMessageDto):
    messageDb = self.messageMappers.createMessageDtoToSqlAlchemyMapper(messageDto)
    return self.messageRepository.update(id, messageDb)

  def delete(self, id):
    messageDb = self.messageRepository.get(id)
    self.messageRepository.delte(messageDb)
    return

  def test(self):
    # message = CreateMessageDto()
    # message.text = "Przykladowa wiaomosc raz dwa trz"
    # message.user_id = 2
    # self.create(message)
    # answer = MessageDto()
    # answer.text = "Test Testowy"
    # self.createAnswer(1,answer)
    # answer.text = "Test 2 Testowy"
    # self.createAnswer(1,answer)
    # print(self.get(1).text)
    # answers = self.getAllAnswers(1)
    # for answer in answers:
    #   print(answer.id)
    #   print(answer.text)