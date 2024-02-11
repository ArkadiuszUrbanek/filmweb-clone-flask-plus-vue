from flask import Blueprint, jsonify, request, send_from_directory
from blueprints import ActorMappers
from blueprints.mappers import ACTOR_FOLDER_PATH
from controllers import HTTP_OK_STATUS, HTTP_CREATED_STATUS
from services import ActorService

actorService = ActorService()
actorMappers = ActorMappers()

actor_blueprint = Blueprint('actor_blueprint', __name__, url_prefix = '/actor')

@actor_blueprint.route('/', methods = ['GET'])
def getAllActor():
  return jsonify(actorService.findAll()), HTTP_OK_STATUS

@actor_blueprint.route('/<int:id>', methods = ['GET'])
def getActor(id):
  return jsonify(actorService.get(id)), HTTP_OK_STATUS

@actor_blueprint.route('/<int:id>/image', methods = ['GET'])
def getActorsImage(id):
  actorFilePath = actorService.findById(id).file_path
  return send_from_directory(ACTOR_FOLDER_PATH, actorFilePath, as_attachment = True), HTTP_OK_STATUS

@actor_blueprint.route('/', methods = ['POST'])
def createActor():
  actorDto = actorMappers.requestToCreateActorDtoMapper(request)
  return jsonify(actorService.create(actorDto)), HTTP_CREATED_STATUS

@actor_blueprint.route('/<int:id>', methods = ['PUT'])
def updateActor(id):
  actorDto = actorMappers.requestToCreateActorDtoMapper(request)
  return jsonify(actorService.update(id, actorDto)), HTTP_OK_STATUS

@actor_blueprint.route('/<int:id>', methods = ['DELETE'])
def deleteActor(id):
  actorService.delete(id)
  return '', HTTP_OK_STATUS