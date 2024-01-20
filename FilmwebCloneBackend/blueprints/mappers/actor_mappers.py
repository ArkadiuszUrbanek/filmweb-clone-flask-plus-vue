from dtos import ActorDto, CreateActorDto
from models import Actor

class ActorMappers():

  def actorSqlAlchemyToDtoMapper(self, actorDb: Actor) -> ActorDto:
    actorDto = ActorDto()
    actorDto.id = actorDb.id
    actorDto.first_name = actorDb.first_name
    actorDto.last_name = actorDb.last_name
    actorDto.nationality = actorDb.nationality
    actorDto.description = actorDb.description
    return actorDto

  def createActorDtoToSqlAlchemyMapper(self, createActorDto: CreateActorDto) -> Actor:
    return Actor(createActorDto.first_name, createActorDto.last_name, createActorDto.nationality, createActorDto.description)