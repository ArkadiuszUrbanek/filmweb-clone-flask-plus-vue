from blueprints import ActorMappers
from dtos import CreateActorDto
from repositories import ActorRepository

class ActorService():

  actorRepository = ActorRepository()
  actorMappers = ActorMappers()

  def findAll(self):
    dtoTab = []
    actorTab = self.actorRepository.findAll()
    convert = lambda unit: self.actorMappers.actorSqlAlchemyToDtoMapper(unit).to_dict()
    for record in actorTab:
      dtoTab.append(convert(record))
    return dtoTab

  def get(self, id):
    actorDb = self.actorRepository.get(id)
    return self.actorMappers.actorSqlAlchemyToDtoMapper(actorDb).to_dict()

  def create(self, actorDto: CreateActorDto):
    actorDb = self.actorMappers.createActorDtoToSqlAlchemyMapper(actorDto)
    return self.actorMappers.actorSqlAlchemyToDtoMapper(self.actorRepository.create(actorDb)).to_dict()

  def update(self, id, actorDto: CreateActorDto):
    actorDb = self.actorMappers.createActorDtoToSqlAlchemyMapper(actorDto)
    return self.actorMappers.actorSqlAlchemyToDtoMapper(self.actorRepository.update(id, actorDb)).to_dict()

  def delete(self, id):
    actorDb = self.actorRepository.get(id)
    self.actorRepository.delete(actorDb)
    return