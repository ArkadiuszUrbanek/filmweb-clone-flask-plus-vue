from .create_review_dto import CreateReviewDto

class ReviewDto(CreateReviewDto):
  id = 0
  creation_date = None
  modification_date = None