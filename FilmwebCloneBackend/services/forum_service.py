from blueprints import ForumMappers
from dtos import CreateForumDto, CreateMessageDto
from repositories import ForumRepository, MessageRepository

class ForumService():

  forumRepository = ForumRepository()
  messageRepository = MessageRepository()
  forumMappers = ForumMappers()

  def findAll(self):
    dtoTab = []
    forumTab = self.forumRepository.findAll()
    convert = lambda unit: self.forumMappers.forumSqlAlchemyToDtoMapper(unit)
    for record in forumTab:
      dtoTab.append(convert(record))
    return dtoTab

  def get(self, id):
    forumDb = self.forumRepository.get(id)
    return self.forumMappers.forumSqlAlchemyToDtoMapper(forumDb)

  def addMessage(self, forumId, messageDto: CreateMessageDto):
    forum = self.forumRepository.get(forumId)
    message = self.messageRepository.create(messageDto)
    message.forum_id = forum.id
    forumMessages = forum.messages
    forumMessages.append(message)
    self.messageRepository.update(message)
    return self.forumRepository.update(forum)

  def create(self, forumDto: CreateForumDto):
    forumDb = self.forumMappers.createForumDtoToSqlAlchemyMapper(forumDto)
    return self.forumRepository.create(forumDb)

  def update(self, id, forumDto: CreateForumDto):
    forumDb = self.forumMappers.createForumDtoToSqlAlchemyMapper(forumDto)
    return self.forumRepository.update(id, forumDb)

  def delete(self, id):
    forumDb = self.forumRepository.get(id)
    self.forumRepository.delete(forumDb)
    return

  def test(self):
    forum = CreateForumDto()
    forum.name = "TestForum"
    forum.description = "Przykladowa wiaomosc raz dwa trz"
    forum.movie_id = 1
    forum.tags = "TestowyHash"
    forum.user_id = 1
    self.create(forum)
    message = CreateMessageDto()
    message.text = "Testowa wiadomosc test"
    message.user_id = 2
    self.addMessage(1,message)
    answer = CreateMessageDto()
    message.text = "Testowa odpowiedz 123"
    message.user_id = 3
    print(self.get(1).text)
    answers = self.getAllAnswers(1)
    for answer in answers:
      print(answer.id)
      print(answer.text)