from flask import Blueprint, jsonify, request
from controllers import HTTP_OK_STATUS, HTTP_CREATED_STATUS
from blueprints import MovieMappers, ReviewMappers
from services import MovieService

movieService = MovieService()
movieMappers = MovieMappers()
reviewMappers = ReviewMappers()

movie_blueprint = Blueprint('movie_blueprint', __name__, url_prefix = '/movie')

@movie_blueprint.route('/', methods = ['GET'])
def getAllMovies():
  return jsonify(movieService.findAll()), HTTP_OK_STATUS

@movie_blueprint.route('/<int:id>', methods = ['GET'])
def getMovie(id):
  return jsonify(movieService.get(id)), HTTP_OK_STATUS

@movie_blueprint.route('/<int:movieId>/review', methods = ['POST'])
def addReview(movieId):
  reviewDto = reviewMappers.requestToCreateReviewDtoMapper(request)
  return jsonify(movieService.addReview(movieId, reviewDto)), HTTP_CREATED_STATUS

@movie_blueprint.route('/', methods = ['POST'])
def createFullMovie():
  movieDto = movieMappers.requestToCreateMovieDtoMapper(request)
  return jsonify(movieService.createFullMovie(movieDto)), HTTP_CREATED_STATUS

@movie_blueprint.route('/plain', methods = ['POST'])
def createPlainMovie():
  movieDto = movieMappers.requestToCreateMovieDtoMapper(request)
  return jsonify(movieService.createPlainMovie(movieDto)), HTTP_CREATED_STATUS

@movie_blueprint.route('/<int:id>', methods = ['PUT'])
def updateMovie(id):
  movieDto = movieMappers.requestToCreateMovieDtoMapper(request)
  return jsonify(movieService.update(id, movieDto)), HTTP_OK_STATUS

@movie_blueprint.route('/<int:id>', methods = ['DELTE'])
def deleteMovie(id):
  movieService.delete(id)
  return '', HTTP_OK_STATUS

@movie_blueprint.route('/<int:movieId>/forums/<int:forumId>', methods = ['PUT'])
def connectForum(movieId, forumId):
  return jsonify(movieService.connectForum(movieId, forumId)), HTTP_OK_STATUS

@movie_blueprint.route('/<int:movieId>/actors', methods = ['PUT'])
def connectActors(movieId):
  actorsIds = request.json.get('actorsIds') if request.json.get('actorsIds') != None else []
  return jsonify(movieService.connectActors(movieId, actorsIds))

@movie_blueprint.route('/<int:movieId>/directors', methods = ['PUT'])
def connectDirectors(movieId):
  directorsIds = request.json.get('directorsIds') if request.json.get('directorsIds') != None else []
  return jsonify(movieService.connectDirectors(movieId, directorsIds))

@movie_blueprint.route('<int:movieId>/genres', methods = ['PUT'])
def connectGenres(movieId):
  genresIds = request.json.get('genresIds') if request.json.get('genresIds') != None else []
  return jsonify(movieService.connectGenres(movieId, genresIds))