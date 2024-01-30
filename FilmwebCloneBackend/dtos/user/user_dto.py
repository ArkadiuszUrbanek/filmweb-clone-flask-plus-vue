class UserDto():
  id = 0
  first_name = ''
  last_name = ''
  email = ''

  def to_dict(self):
    return {
      'id' : str(self.id),
      'first_name' : self.first_name,
      'last_name' : self.last_name,
      'email' : self.email,
    }

