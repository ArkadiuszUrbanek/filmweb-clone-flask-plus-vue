from .create_genre_dto import CreateGenreDto

class GenreDto(CreateGenreDto):
 id = 0

 def to_dict(self):
  return {
   'id' : str(self.id),
   'name' : str(self.name),
  }