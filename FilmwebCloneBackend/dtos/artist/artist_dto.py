from .create_artist_dto import CreateArtistDto

class ArtistDto(CreateArtistDto):
  id = 0

  def to_dict(self):
    return {
      'id' : str(self.id),
      'first_name' : self.first_name,
      'last_name' : self.last_name,
      'nationality' : self.nationality,
      'description' : self.description,
    }