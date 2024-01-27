from flask import Blueprint, jsonify, request
from controllers import HTTP_OK_STATUS
from blueprints import ReviewMappers
from services import ReviewService

reviewService = ReviewService()
reviewMappers = ReviewMappers()

review_blueprint = Blueprint('review_blueprint', __name__, url_prefix='/review')

@review_blueprint.route('/<int:id>', methods = ['GET'])
def getReview(id):
  return jsonify(reviewService.get(id)), HTTP_OK_STATUS

@review_blueprint.route('/<int:id>', methods=['PUT'])
def updateReview(id):
  reviewDto = reviewMappers.reviewSqlAlchemyToDtoMapper(request)
  return jsonify(reviewService.update(id, reviewDto)), HTTP_OK_STATUS

@review_blueprint.route('/<int:id>', methods=['DELETE'])
def deleteReview(id):
  reviewService.delete(id)
  return '', HTTP_OK_STATUS
