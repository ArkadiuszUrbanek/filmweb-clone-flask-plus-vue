from flask import Request
from dtos import ForumDto, CreateForumDto
from models import Forum

from .message_mappers import MessageMappers

class ForumMappers():

  def requestToCreateForumDtoMapper(self, request: Request) -> CreateForumDto:
     createForumDto = CreateForumDto()
     createForumDto.name = request.json.get('name') if request.json.get('name') != None else ''
     createForumDto.description = request.json.get('description') if request.json.get('description') != None else ''
     createForumDto.tags = request.json.get('tags') if request.json.get('tags') != None else ''
     createForumDto.user_id = request.json.get('user_id') if request.json.get('user_id') != None else 0
     createForumDto.movie_id = request.json.get('movie_id') if request.json.get('movie_id') != None else 0
     return createForumDto

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