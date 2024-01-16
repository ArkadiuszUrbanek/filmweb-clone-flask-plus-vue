from dtos import ReviewDto, CreateReviewDto
from models import Review

class ReviewMappers():

  def reviewSqlAlchemyToDtoMapper(self, reviewDb: Review) -> ReviewDto:
    reviewDto = ReviewDto()
    reviewDto.id = reviewDb.id
    reviewDto.mark = reviewDb.mark
    reviewDto.description = reviewDb.description
    reviewDto.creation_date = reviewDb.creation_date
    reviewDto.modification_date = reviewDb.modification_date
    reviewDto.user_id = reviewDb.user_id
    reviewDto.movie_id = reviewDb.movie_id
    return reviewDto

  def createReviewDtoToSqlAlchemyMapper(self, createReviewDto: CreateReviewDto):
    return Review(createReviewDto.mark, createReviewDto.description, createReviewDto.user_id, createReviewDto.movie_id)