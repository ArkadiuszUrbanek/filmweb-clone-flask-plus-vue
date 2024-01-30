from blueprints import UserMappers
from dtos import CreateUserDto
from repositories import UserRepository

class UserService():

  userRepository = UserRepository()
  userMappers = UserMappers()

  def findAll(self):
    dtoTab = []
    userTab = self.userRepository.findAll()
    convert = lambda unit : self.userMappers.userSqlAlchemyToDtoMapper(unit).to_dict()
    for record in userTab:
        dtoTab.append(convert(record))
    return dtoTab

  def get(self, id):
    dbUser = self.userRepository.get(id)
    return self.userMappers.userSqlAlchemyToDtoMapper(dbUser).to_dict()

  def create(self, userDto: CreateUserDto):
    userDb = self.userMappers.createUserDtoToSqlAlchemyMapper(userDto)
    return self.userMappers.userSqlAlchemyToDtoMapper(self.userRepository.create(userDb)).to_dict()

  def update(self, id, userDto: CreateUserDto):
    userDb = self.userMappers.createUserDtoToSqlAlchemyMapper(userDto)
    return self.userMappers.userSqlAlchemyToDtoMapper(self.userRepository.update(id, userDb)).to_dict()

  def delete(self, id):
    userDb = self.userRepository.get(id)
    self.userRepository.delete(userDb)
    return

