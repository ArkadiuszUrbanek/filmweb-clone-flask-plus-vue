from flask import Request
from dtos import ReviewDto, CreateReviewDto
from models import Review

class ReviewMappers():

  def requestToCreateReviewDtoMapper(self, request: Request) -> CreateReviewDto:
    createReviewDto = CreateReviewDto()
    createReviewDto.mark = request.json.get('mark') if request.json.get('mark') != None else 0
    createReviewDto.description = request.json.get('description') if request.json.get('description') != None else ''
    createReviewDto.user_id = request.json.get('user_id') if request.json.get('user_id') != None else 0
    createReviewDto.movie_id = request.json.get('movie_id') if request.json.get('movie_id') != None else 0
    return createReviewDto

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