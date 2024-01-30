from blueprints import ReviewMappers
from dtos import CreateReviewDto
from repositories import ReviewRepository

class ReviewService():

  reviewRepository = ReviewRepository()
  reviewMappers = ReviewMappers()

  def get(self, id):
    reviewDb = self.reviewRepository.get(id)
    return self.reviewMappers.reviewSqlAlchemyToDtoMapper(reviewDb).to_dict()

  def update(self, id, reviewDto: CreateReviewDto):
    reviewDb = self.reviewMappers.createReviewDtoToSqlAlchemyMapper(reviewDto)
    return self.reviewMappers.reviewSqlAlchemyToDtoMapper(self.reviewRepository.update(id, reviewDb)).to_dict()

  def delete(self, id):
    reviewDb = self.reviewRepository.get(id)
    self.reviewRepository.delete(reviewDb)
    return