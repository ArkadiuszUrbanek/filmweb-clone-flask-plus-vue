from blueprints import ReviewMappers
from dtos import CreateReviewDto
from repositories import ReviewRepository

class ReviewService():

  reviewRepository = ReviewRepository()
  reviewMappers = ReviewMappers()

  def get(self, id):
    reviewDb = self.reviewRepository.get(id)
    return self.reviewMappers.reviewSqlAlchemyToDtoMapper(reviewDb)

  def update(self, id, reviewDto: CreateReviewDto):
    reviewDb = self.reviewMappers.createReviewDtoToSqlAlchemyMapper(reviewDto)
    return self.reviewRepository.update(id, reviewDb)

  def delete(self, id):
    reviewDb = self.reviewRepository.get(id)
    self.reviewRepository.delete(reviewDb)
    return