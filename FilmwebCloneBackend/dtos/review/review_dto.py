from .create_review_dto import CreateReviewDto

class ReviewDto(CreateReviewDto):
  id = 0
  creation_date = None
  modification_date = None

  def to_dict(self):
    return {
      'id' : str(self.id),
      'mark' : str(self.mark),
      'description' : self.description,
      'user_id' : str(self.user_id),
      'movie_id' : str(self.movie_id),
      'creation_date' : str(self.creation_date),
      'modification_date' : str(self.modification_date),
    }