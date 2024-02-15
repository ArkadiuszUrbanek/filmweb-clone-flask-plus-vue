from flask import Request
from enums import UserAccountType, UserRole, UserGender
from models import User
from dtos import UserDto, CreateUserDto

class UserMappers():

  def requestToCreateUserDtoMapper(self, request: Request) -> CreateUserDto:
    createUserDto = CreateUserDto()
    createUserDto.first_name = request.json.get('first_name') if request.json.get('first_name') != None else ''
    createUserDto.last_name = request.json.get('last_name') if request.json.get('last_name') != None else ''
    createUserDto.email = request.json.get('email') if request.json.get('email') != None else ''
    createUserDto.password_hash = request.json.get('password_hash') if  request.json.get('password_hash') != None else ''
    createUserDto.gender = request.json.get('gender') if request.json.get('gender') != None else UserGender.MALE
    createUserDto.account_type = request.json.get('account_type') if request.json.get('account_type') != None else UserAccountType.APP
    createUserDto.role = request.json.get('role') if request.json.get('role') != None else UserRole.GUEST
    return createUserDto

  def userSqlAlchemyToDtoMapper(self, userDb: User) -> UserDto:
    userDto = UserDto()
    userDto.id = userDb.id
    userDto.first_name = userDb.first_name
    userDto.last_name = userDb.last_name
    userDto.email = userDb.email
    userDto.gender = userDb.gender
    userDto.account_type = userDb.account_type
    userDto.role = userDb.role
    return userDto

  def createUserDtoToSqlAlchemyMapper(self, createUserDto: CreateUserDto) -> User:
    return User(createUserDto.first_name,
                createUserDto.last_name,
                createUserDto.email,
                createUserDto.gender,
                createUserDto.password_hash,
                createUserDto.account_type,
                createUserDto.role)