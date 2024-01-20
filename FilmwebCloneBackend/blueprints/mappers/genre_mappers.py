from dtos import GenreDto, CreateGenreDto
from models import Genre

class GenreMappers():

  def genreSqlAlchemyToDtoMapper(self, genreDb: Genre) -> GenreDto:
    genreDto = GenreDto()
    genreDto.id = genreDb.id
    genreDto.name = genreDb.name
    return genreDto

  def createGenreDtoToSqlAlchemyMapper(self, createGenreDto: CreateGenreDto) -> Genre:
    return Genre(createGenreDto.name)