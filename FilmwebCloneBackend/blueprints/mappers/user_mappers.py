from models.user import User
from dtos import UserDto, CreateUserDto

class UserMappers():

  def userSqlAlchemyToDtoMapper(self, userDb: User) -> UserDto:
    userDto = UserDto()
    userDto.id = userDb.id
    userDto.first_name = userDb.first_name
    userDto.last_name = userDb.last_name
    userDto.email = userDb.email
    return userDto

  def createUserDtoToSqlAlchemyMapper(self, createUserDto: CreateUserDto) -> User:
    return User(createUserDto.first_name,
                createUserDto.last_name,
                createUserDto.email,
                createUserDto.password_hash,
                createUserDto.account_type,
                createUserDto.role)