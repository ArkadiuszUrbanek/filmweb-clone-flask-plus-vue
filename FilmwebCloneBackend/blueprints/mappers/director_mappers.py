from dtos import DirectorDto, CreateDirectorDto
from models import Director

class DirectorMappers():

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