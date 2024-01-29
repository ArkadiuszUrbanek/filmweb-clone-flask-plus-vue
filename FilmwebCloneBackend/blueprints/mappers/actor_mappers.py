from flask import Request
from dtos import ActorDto, CreateActorDto
from models import Actor

class ActorMappers():

  def requestToCreateActorDtoMapper(self, request: Request) -> CreateActorDto:
    createActorDto = CreateActorDto()
    createActorDto.first_name = request.json.get('first_name') if request.json.get('first_name') != None else ''
    createActorDto.last_name = request.json.get('last_name') if request.json.get('last_name') != None else ''
    createActorDto.nationality = request.json.get('nationality') if request.json.get('nationality') != None else ''
    createActorDto.description = request.json.get('description') if request.json.get('description') != None else ''
    return createActorDto

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