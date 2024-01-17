from blueprints import GenreMappers
from dtos import CreateGenreDto
from repositories import GenreRepository

class GenreService():

  genreRepository = GenreRepository()
  genreMappers = GenreMappers()

  def findAll(self):
    dtoTab = []
    genreTab = self.genreRepository.findAll()
    convert = lambda unit: self.genreMappers.genreSqlAlchemyToDtoMapper(unit)
    for record in genreTab:
      dtoTab.append(convert(record))
    return dtoTab

  def get(self, id):
    genreDb = self.genreRepository.get(id)
    return self.genreMappers.genreSqlAlchemyToDtoMapper(genreDb)

  def create(self, genreDto: CreateGenreDto):
    genreDb = self.genreMappers.createGenreDtoToSqlAlchemyMapper(genreDto)
    return self.genreRepository.create(genreDb)

  def update(self, id, genreDto: CreateGenreDto):
    genreDb = self.genreMappers.createGenreDtoToSqlAlchemyMapper(genreDto)
    return self.genreRepository.update(id, genreDb)

  def delete(self, id):
    genreDb = self.genreRepository.get(id)
    self.genreRepository.delete(genreDb)
    return