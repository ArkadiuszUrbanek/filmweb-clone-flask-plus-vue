from flask import Request
from dtos import GenreDto, CreateGenreDto
from models import Genre

class GenreMappers():

  def requestToCreateGenreDtoMapper(self, request: Request) -> CreateGenreDto:
    createGenreDto = CreateGenreDto()
    createGenreDto.name = request.json.get('name') if request.json.get('name') != None else ''
    return createGenreDto

  def genreSqlAlchemyToDtoMapper(self, genreDb: Genre) -> GenreDto:
    genreDto = GenreDto()
    genreDto.id = genreDb.id
    genreDto.name = genreDb.name
    return genreDto

  def createGenreDtoToSqlAlchemyMapper(self, createGenreDto: CreateGenreDto) -> Genre:
    return Genre(createGenreDto.name)