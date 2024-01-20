from blueprints import DirectorMappers
from dtos import CreateDirectorDto
from repositories import DirectorRepository

class DirectorService():

  directorRepository = DirectorRepository()
  directorMappers = DirectorMappers()

  def findAll(self):
    dtoTab = []
    directorTab = self.directorRepository.findAll()
    convert = lambda unit: self.directorMappers.directorSqlAlchemyToDtoMapper(unit)
    for record in directorTab:
      dtoTab.append(convert(record))
    return dtoTab

  def get(self, id):
    directorDb = self.directorRepository.get(id)
    return self.directorMappers.directorSqlAlchemyToDtoMapper(directorDb)

  def create(self, directorDto: CreateDirectorDto):
    directorDb = self.directorMappers.createDirectorDtoToSqlAlchemyMapper(directorDto)
    return self.directorRepository.create(directorDb)

  def update(self, id, directorDto: CreateDirectorDto):
    directorDb = self.directorMappers.createDirectorDtoToSqlAlchemyMapper(directorDto)
    return self.directorRepository.update(id, directorDb)

  def delete(self, id):
    directorDb = self.directorRepository.get(id)
    self.directorRepository.delete(directorDb)
    return