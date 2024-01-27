from enums import UserAccountType, UserRole
from models import User
from dtos import UserDto, CreateUserDto

class UserMappers():

  def requestToCreateUserDtoMapper(self, request) -> CreateUserDto:
    createUserDto = CreateUserDto()
    createUserDto.first_name = request.form['first_name'] if request.form['first_name'] != None else ''
    createUserDto.last_name = request.form['last_name'] if request.form['last_name'] != None else ''
    createUserDto.email = request.form['email'] if request.form['email'] != None else ''
    createUserDto.password_hash = request.form['password_hash'] if  request.form['password_hash'] != None else ''
    createUserDto.account_type = request.form['account_type'] if request.form['account_type'] != None else UserAccountType.APP
    createUserDto.role = request.form['role'] if request.form['role'] != None else UserRole.GUEST
    return createUserDto

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