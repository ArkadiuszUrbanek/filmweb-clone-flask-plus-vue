from enums import UserAccountType, UserRole
from .user_dto import UserDto

class CreateUserDto(UserDto):
  password_hash = ''
  account_type = UserAccountType.APP
  role = UserRole.GUEST