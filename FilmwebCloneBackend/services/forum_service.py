from blueprints import ForumMappers, MessageMappers
from dtos import CreateForumDto, CreateMessageDto
from repositories import ForumRepository, MessageRepository

class ForumService():

  forumRepository = ForumRepository()
  messageRepository = MessageRepository()
  forumMappers = ForumMappers()
  messageMappers = MessageMappers()

  def findAll(self):
    dtoTab = []
    forumTab = self.forumRepository.findAll()
    convert = lambda unit: self.forumMappers.forumSqlAlchemyToDtoMapper(unit).to_dict()
    for record in forumTab:
      dtoTab.append(convert(record))
    return dtoTab

  def get(self, id):
    forumDb = self.forumRepository.get(id)
    return self.forumMappers.forumSqlAlchemyToDtoMapper(forumDb)

  def addMessage(self, forumId, messageDto: CreateMessageDto):
    forum = self.forumRepository.get(forumId)
    message = self.messageRepository.create(forum.id, self.messageMappers.createMessageDtoToSqlAlchemyMapper(messageDto))
    forumMessages = forum.messages
    forumMessages.append(message)
    return self.forumMappers.forumSqlAlchemyToDtoMapper(self.forumRepository.update(forum.id, forum)).to_dict()

  def create(self, forumDto: CreateForumDto):
    forumDb = self.forumMappers.createForumDtoToSqlAlchemyMapper(forumDto)
    return self.forumMappers.forumSqlAlchemyToDtoMapper(self.forumRepository.create(forumDb)).to_dict()

  def update(self, id, forumDto: CreateForumDto):
    forumDb = self.forumMappers.createForumDtoToSqlAlchemyMapper(forumDto)
    return self.forumMappers.forumSqlAlchemyToDtoMapper(self.forumRepository.update(id, forumDb)).to_dict()

  def delete(self, id):
    forumDb = self.forumRepository.get(id)
    self.forumRepository.delete(forumDb)
    return