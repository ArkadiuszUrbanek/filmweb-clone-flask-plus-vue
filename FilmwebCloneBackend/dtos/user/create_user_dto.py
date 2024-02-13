from enums import UserAccountType, UserRole

class CreateUserDto():
  first_name = ''
  last_name = ''
  email = ''
  gender = ''
  password_hash = ''
  account_type = UserAccountType.APP
  role = UserRole.GUEST