from .create_movie_dto import CreateMovieDto

class MovieDto(CreateMovieDto):
  id = 0
  reviews_count = 0
  average_rating = 0

  def to_dict(self):
    return {
      'id' : str(self.id),
      'title' : self.title,
      'subtitle' : self.subtitle,
      'premiere_date' : str(self.premiere_date),
      'length_time' : str(self.length_time),
      'description' : self.description,
      'reviews' : [review.to_dict() for review in self.reviews],
      'forums' : [forum.to_dict() for forum in self.forums],
      'directors' : [director.to_dict() for director in self.directors],
      'actors' : [actor.to_dict() for actor in self.actors],
      'genres' : [genre.to_dict() for genre in self.genres],
      'reviews_count' : str(self.reviews_count),
      'average_rating' : str(self.average_rating),
    }
