from flask import Blueprint, jsonify, request
from controllers import HTTP_OK_STATUS, HTTP_CREATED_STATUS
from blueprints import GenreMappers
from services import GenreService

genreService = GenreService()
genreMappers = GenreMappers()

genre_blueprint = Blueprint('genre_bluteprint', __name__, url_prefix = '/genre')

@genre_blueprint.route('/', methods = ['GET'])
def getAllGenres():
  return jsonify(genreService.findAll()), HTTP_OK_STATUS

@genre_blueprint.route('/<int:id>', methods = ['GET'])
def getGenre(id):
  return jsonify(genreService.get(id)), HTTP_OK_STATUS

@genre_blueprint.route('/', methods = ['POST'])
def createGenre():
  genreDto = genreMappers.requestToCreateGenreDtoMapper(request)
  return jsonify(genreService.create(genreDto)), HTTP_CREATED_STATUS

@genre_blueprint.route('/<int:id>', methods = ['PUT'])
def updateGenre(id):
  genreDto = genreMappers.requestToCreateGenreDtoMapper(request)
  return jsonify(genreService.update(id, genreDto)), HTTP_OK_STATUS

@genre_blueprint.route('/<int:id>', methods = ['DELETE'])
def deleteGenre(id):
  genreService.delete(id)
  return '', HTTP_OK_STATUS