from enums import UserAccountType, UserRole, UserGender

class UserDto():
  id = 0
  first_name = ''
  last_name = ''
  email = ''
  gender = UserGender.MALE
  account_type = UserAccountType.APP
  role = UserRole.GUEST

  def to_dict(self):
    return {
      'id' : str(self.id),
      'first_name' : self.first_name,
      'last_name' : self.last_name,
      'email' : self.email,
      'gender' : str(self.gender),
      'account_type' : str(self.account_type),
      'role' : str(self.role),
    }

