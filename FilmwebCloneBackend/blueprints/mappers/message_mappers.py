from flask import Request
from dtos import MessageDto, CreateMessageDto
from repositories import UserRepository
from models import Message, User

class MessageMappers():

  def requestToCreateMessageDtoMapper(self, request: Request) -> CreateMessageDto:
    createMessageDto = CreateMessageDto()
    createMessageDto.text = request.json.get('text') if request.json.get('text') != None else ''
    createMessageDto.user_id = request.json.get('user_id') if request.json.get('user_id') != None else 0
    createMessageDto.forum_id = request.json.get('forum_id') if request.json.get('forum_id') != None else 0
    return createMessageDto

  def messageSqlAlchemyToDtoMapper(self, messageDb: Message) -> MessageDto:
    userRepository = UserRepository()
    messageDto = MessageDto()
    messageDto.id = messageDb.id
    messageDto.text = messageDb.text
    messageDto.forum_id = messageDb.forum_id
    messageDto.user_id = messageDb.user_id
    userDb: User = userRepository.get(messageDb.user_id)
    messageDto.user_first_name = userDb.first_name
    messageDto.user_last_name = userDb.last_name
    messageDto.user_gender = userDb.gender
    messageDto.main_message_id = messageDb.main_message
    messageDto.creation_date = messageDb.creation_date
    messageDto.modification_date = messageDb.modification_date
    messageDto.messages = None
    if messageDb.messages != None:
        messageDto.messages = MessageDto()
        messageDto.messages.id = messageDb.messages.id
        messageDto.messages.text = messageDb.messages.text
        messageDto.messages.forum_id = messageDb.messages.forum_id
        messageDto.messages.user_id = messageDb.messages.user_id
        messageDto.messages.main_message_id = messageDb.messages.main_message
        messageDto.messages.creation_date = messageDb.messages.creation_date
        messageDto.messages.modification_date = messageDb.messages.modification_date
    return messageDto

  def createMessageDtoToSqlAlchemyMapper(self, createMessageDto: CreateMessageDto) -> Message:
    return Message(createMessageDto.text, createMessageDto.user_id)