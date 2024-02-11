from flask import Blueprint, jsonify, request, send_from_directory
from blueprints import DirectorMappers
from blueprints.mappers import DIRECTOR_FOLDER_PATH
from controllers import HTTP_OK_STATUS, HTTP_CREATED_STATUS
from services import DirectorService

directorService = DirectorService()
directorMappers = DirectorMappers()

director_blueprint = Blueprint('director_blueprint', __name__, url_prefix = '/director')

@director_blueprint.route('/', methods = ['GET'])
def getAllDirectors():
  return jsonify(directorService.findAll()), HTTP_OK_STATUS

@director_blueprint.route('/<int:id>', methods = ['GET'])
def getDirector(id):
  return jsonify(directorService.get(id)), HTTP_OK_STATUS

@director_blueprint.route('/<int:id>/image', methods = ['GET'])
def getDirectorsImage(id):
  directorFilePath = directorService.findById(id).file_path
  return send_from_directory(DIRECTOR_FOLDER_PATH, directorFilePath, as_attachment = True), HTTP_OK_STATUS

@director_blueprint.route('/', methods = ['POST'])
def createDirector():
  directorDto = directorMappers.requestToCreateDirectorDtoMapper(request)
  return jsonify(directorService.create(directorDto)), HTTP_CREATED_STATUS

@director_blueprint.route('/<int:id>', methods = ['PUT'])
def updateDirector(id):
  directorDto = directorMappers.requestToCreateDirectorDtoMapper(request)
  return jsonify(directorService.update(id,directorDto)), HTTP_OK_STATUS

@director_blueprint.route('/<int:id>', methods = ['DELETE'])
def deleteDirector(id):
  directorService.delete(id)
  return '', HTTP_OK_STATUS