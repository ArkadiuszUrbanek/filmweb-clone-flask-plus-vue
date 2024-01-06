from models import Message
from dtos import MessageDto

class MessageMappers():

  def messageSqlAlchemyToDtoMapper(self, messageDb: Message) -> MessageDto:
    messageDto = MessageDto()
    messageDto.id = messageDb.id
    messageDto.text = messageDb.text
    return messageDto

  def messageDtoToSqlAlchemyMapper(self, messageDto: MessageDto) -> Message:
    return Message(messageDto.text)