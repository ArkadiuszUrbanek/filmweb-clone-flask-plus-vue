from flask import Request
from dtos import DirectorDto, CreateDirectorDto
from models import Director

class DirectorMappers():

  def requestToCreateDirectorDtoMapper(self, request: Request) -> CreateDirectorDto:
    createDirectorDto = CreateDirectorDto()
    createDirectorDto.first_name = request.json.get('first_name') if request.json.get('first_name') != None else ''
    createDirectorDto.last_name = request.json.get('last_name') if request.json.get('last_name') != None else ''
    createDirectorDto.nationality = request.json.get('nationality') if request.json.get('nationality') != None else ''
    createDirectorDto.description = request.json.get('description') if request.json.get('description') != None else ''
    return createDirectorDto

  def directorSqlAlchemyToDtoMapper(self, directorDb: Director) -> DirectorDto:
    directorDto = DirectorDto()
    directorDto.id = directorDb.id
    directorDto.first_name = directorDb.first_name
    directorDto.last_name = directorDb.last_name
    directorDto.nationality = directorDb.nationality
    directorDto.description = directorDb.description
    return directorDto

  def createDirectorDtoToSqlAlchemyMapper(self, createDirectorDto: CreateDirectorDto) -> Director:
    return Director(createDirectorDto.first_name, createDirectorDto.last_name, createDirectorDto.nationality, createDirectorDto.description)