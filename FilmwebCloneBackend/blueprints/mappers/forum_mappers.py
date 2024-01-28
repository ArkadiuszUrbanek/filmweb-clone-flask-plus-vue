from dtos import ForumDto, CreateForumDto
from models import Forum

from .message_mappers import MessageMappers

class ForumMappers():

  def forumSqlAlchemyToDtoMapper(self, forumDb: Forum) -> ForumDto:
    messageMappers = MessageMappers()
    forumDto = ForumDto()
    forumDto.id = forumDb.id
    forumDto.name = forumDb.name
    forumDto.description = forumDb.description
    forumDto.tags = forumDb.tags
    forumDto.creation_date = forumDb.creation_date
    forumDto.modification_date = forumDb.modification_date
    forumDto.messages = []
    for message in forumDb.messages:
         forumDto.messages.append(messageMappers.messageSqlAlchemyToDtoMapper(message))
    forumDto.user_id = forumDb.user_id
    forumDto.movie_id = forumDb.movie_id
    return forumDto

  def createForumDtoToSqlAlchemyMapper(self, createForumDto: CreateForumDto) -> Forum:
    return Forum(createForumDto.name, createForumDto.description, createForumDto.tags, createForumDto.user_id, createForumDto.movie_id)