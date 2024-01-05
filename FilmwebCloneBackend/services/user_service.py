from blueprints import UserMappers
from dtos import CreateUserDto
from repositories import UserRepository

class UserService():

  userRepository = UserRepository()
  userMappers = UserMappers()

  def findAll(self):
    dtoTab = []
    userTab = self.userRepository.findAll()
    convert = lambda unit : self.userMappers.userSqlAlchemyToDtoMapper(unit)
    for record in userTab:
        dtoTab.append(convert(record))
    return dtoTab

  def get(self, id):
    dbUser = self.userRepository.get(id)
    return self.userMappers.userSqlAlchemyToDtoMapper(dbUser)

  def create(self, userDto: CreateUserDto):
    userDb = self.userMappers.createUserDtoToSqlAlchemyMapper(userDto)
    return self.userRepository.create(userDb)

  def update(self, id, userDto: CreateUserDto):
    userDb = self.userMappers.createUserDtoToSqlAlchemyMapper(userDto)
    return self.userRepository.update(id, userDb)

  def delete(self, id):
    userDb = self.userRepository.get(id)
    self.userRepository.delete(userDb)
    return

