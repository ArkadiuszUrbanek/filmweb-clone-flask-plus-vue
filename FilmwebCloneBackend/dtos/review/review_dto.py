from .create_review_dto import CreateReviewDto
from enums import UserGender

class ReviewDto(CreateReviewDto):
  id = 0
  user_first_name = ''
  user_last_name = ''
  user_gender = UserGender.MALE
  creation_date = None
  modification_date = None

  def to_dict(self):
    return {
      'id' : str(self.id),
      'mark' : str(self.mark),
      'description' : self.description,
      'user_id' : str(self.user_id),
      'user_first_name' : self.user_first_name,
      'user_last_name' : self.user_last_name,
      'user_gender' : str(self.user_gender),
      'movie_id' : str(self.movie_id),
      'creation_date' : str(self.creation_date),
      'modification_date' : str(self.modification_date),
    }