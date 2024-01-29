from blueprints import GenreMappers
from dtos import CreateGenreDto
from repositories import GenreRepository

class GenreService():

  genreRepository = GenreRepository()
  genreMappers = GenreMappers()

  def findAll(self):
    dtoTab = []
    genreTab = self.genreRepository.findAll()
    convert = lambda unit: self.genreMappers.genreSqlAlchemyToDtoMapper(unit).to_dict()
    for record in genreTab:
      dtoTab.append(convert(record))
    return dtoTab

  def get(self, id):
    genreDb = self.genreRepository.get(id)
    return self.genreMappers.genreSqlAlchemyToDtoMapper(genreDb).to_dict()

  def create(self, genreDto: CreateGenreDto):
    genreDb = self.genreMappers.createGenreDtoToSqlAlchemyMapper(genreDto)
    return self.genreMappers.genreSqlAlchemyToDtoMapper(self.genreRepository.create(genreDb)).to_dict()

  def update(self, id, genreDto: CreateGenreDto):
    genreDb = self.genreMappers.createGenreDtoToSqlAlchemyMapper(genreDto)
    return self.genreMappers.genreSqlAlchemyToDtoMapper(self.genreRepository.update(id, genreDb)).to_dict()

  def delete(self, id):
    genreDb = self.genreRepository.get(id)
    self.genreRepository.delete(genreDb)
    return