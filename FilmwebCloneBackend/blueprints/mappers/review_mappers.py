from flask import Request
from dtos import ReviewDto, CreateReviewDto
from repositories import UserRepository
from models import Review, User

class ReviewMappers():

  def requestToCreateReviewDtoMapper(self, request: Request) -> CreateReviewDto:
    createReviewDto = CreateReviewDto()
    createReviewDto.mark = request.json.get('mark') if request.json.get('mark') != None else 0
    createReviewDto.description = request.json.get('description') if request.json.get('description') != None else ''
    createReviewDto.user_id = request.json.get('user_id') if request.json.get('user_id') != None else 0
    createReviewDto.movie_id = request.json.get('movie_id') if request.json.get('movie_id') != None else 0
    return createReviewDto

  def reviewSqlAlchemyToDtoMapper(self, reviewDb: Review) -> ReviewDto:
    userRepository = UserRepository()
    userDb: User = userRepository.get(reviewDb.user_id)
    reviewDto = ReviewDto()
    reviewDto.id = reviewDb.id
    reviewDto.mark = reviewDb.mark
    reviewDto.description = reviewDb.description
    reviewDto.creation_date = reviewDb.creation_date
    reviewDto.modification_date = reviewDb.modification_date
    reviewDto.user_id = reviewDb.user_id
    reviewDto.movie_id = reviewDb.movie_id
    reviewDto.user_first_name = userDb.first_name
    reviewDto.user_last_name = userDb.last_name
    reviewDto.user_gender = userDb.gender
    return reviewDto

  def createReviewDtoToSqlAlchemyMapper(self, createReviewDto: CreateReviewDto):
    return Review(createReviewDto.mark, createReviewDto.description, createReviewDto.user_id, createReviewDto.movie_id)