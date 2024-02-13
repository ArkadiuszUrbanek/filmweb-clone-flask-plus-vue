import math
from datetime import datetime
from typing import List
from flask import Request
from dtos import ForumDto, CreateForumDto, ForumPagedDto, ForumPaginationParameters
from models import Forum, User
from repositories import UserRepository

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
    userRepository = UserRepository()
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
    userDb: User = userRepository.get(forumDb.user_id)
    forumDto.user_first_name = userDb.first_name
    forumDto.user_last_name = userDb.last_name
    forumDto.movie_id = forumDb.movie_id
    return forumDto

  def createForumDtoToSqlAlchemyMapper(self, createForumDto: CreateForumDto) -> Forum:
    return Forum(createForumDto.name, createForumDto.description, createForumDto.tags, createForumDto.user_id, createForumDto.movie_id)

  def sortForumsByKey(self, chosenForums, sorting_property, sorting_order):
    sortingReverse = False
    if (sorting_order == 'asc'):
        sortingReverse = True

    if(sorting_property == 'id'):
      return sorted(chosenForums, key = lambda forum : int(forum.get('id', 0)), reverse = sortingReverse)
    elif(sorting_property == 'name'):
      return sorted(chosenForums, key = lambda forum : str(forum.get('name', 1)), reverse = sortingReverse)
    elif(sorting_property == 'description'):
      return sorted(chosenForums, key = lambda forum : str(forum.get('description', 2)), reverse = sortingReverse)
    elif(sorting_property == 'tags'):
      return sorted(chosenForums, key = lambda forum : str(forum.get('tags', 3)), reverse = sortingReverse)
    elif(sorting_property == 'creation_date'):
      return sorted(chosenForums, key = lambda forum : datetime.strptime(forum.get('creation_date', 4), '%Y-%m-%d %H:%M:%S'), reverse = sortingReverse)
    elif(sorting_property == 'modification_date'):
      return sorted(chosenForums, key = lambda forum : datetime.strptime(forum.get('modification_date', 5), '%Y-%m-%d %H:%M:%S'), reverse = sortingReverse)
    elif(sorting_property == 'messages_count'):
        return sorted(chosenForums, key = lambda forum : int(forum.get('messages_count', 7)), reverse = sortingReverse)
    return dict(chosenForums)

  def forumDtoTableToForumPagedDto(self, forumsDto: List[ForumDto], pagination: ForumPaginationParameters) -> ForumPagedDto:
    forumPage = ForumPagedDto()
    forumPage.results_count = len(forumsDto)
    if pagination.page_size != 0:
        forumPage.pages_count = math.ceil(len(forumsDto) / int(pagination.page_size))
    if pagination.page_number == 0:
       pagination.page_number = 1
    firstElement = (int(pagination.page_number)-1) * int(pagination.page_size)
    lastElement = firstElement + int(pagination.page_size)
    chosenForums = forumsDto[firstElement : lastElement]
    forumPage.current_page_results_count = len(chosenForums)
    print(chosenForums)
    chosenForums = self.sortForumsByKey(chosenForums, pagination.sorting_property, pagination.sorting_order)
    forumPage.forums = chosenForums
    print(chosenForums)
    return forumPage

  def requestToForumPaginationParamerers(self, request: Request) -> ForumPaginationParameters:
    forumPaginationParameters = ForumPaginationParameters()
    forumPaginationParameters.page_number = request.args.get('page_number') if request.args.get('page_number') != None else 0
    forumPaginationParameters.page_size = request.args.get('page_size') if request.args.get('page_size') != None else 10
    forumPaginationParameters.sorting_property = request.args.get('sorting_property') if request.args.get('sorting_property') != None else 'id'
    forumPaginationParameters.sorting_order = request.args.get('sorting_order') if request.args.get('sorting_order') != None else 'asc'
    return forumPaginationParameters