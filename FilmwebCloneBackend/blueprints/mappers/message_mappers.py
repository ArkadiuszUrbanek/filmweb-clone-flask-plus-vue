from dtos import MessageDto, CreateMessageDto
from models import Message

class MessageMappers():

  def messageSqlAlchemyToDtoMapper(self, messageDb: Message) -> MessageDto:
    messageDto = MessageDto()
    messageDto.id = messageDb.id
    messageDto.text = messageDb.text
    messageDto.forum_id = messageDb.forum_id
    messageDto.user_id = messageDb.user_id
    messageDto.main_message_id = messageDb.main_message
    messageDto.messages = messageDb.messages
    messageDto.creation_date = messageDb.creation_date
    messageDto.modification_date = messageDb.modification_date
    return messageDto

  def createMessageDtoToSqlAlchemyMapper(self, createMessageDto: CreateMessageDto) -> Message:
    return Message(createMessageDto.text, createMessageDto.user_id)