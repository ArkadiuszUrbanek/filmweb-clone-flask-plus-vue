from .create_artist_dto import CreateArtistDto

class ArtistDto(CreateArtistDto):
  id = 0

  def to_dict(self):
    return {
      'id' : str(self.id),
      'first_name' : self.first_name,
      'last_name' : self.last_name,
      'nationality' : self.nationality,
      'gender' : str(self.gender),
      'height' : str(self.height),
      'birth_date' : str(self.birth_date),
      'description' : self.description,
      'file_path' : self.file_path,
    }