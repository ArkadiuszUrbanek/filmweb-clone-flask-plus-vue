from enums import UserGender
class CreateArtistDto():
  first_name = ''
  last_name = ''
  nationality = ''
  gender = UserGender.MALE
  height = 0
  birth_date = None
  file_path = ''
  description = ''