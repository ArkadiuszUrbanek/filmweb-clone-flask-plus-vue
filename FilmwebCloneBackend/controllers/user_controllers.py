from flask import Blueprint, jsonify, request
from controllers import HTTP_OK_STATUS, HTTP_CREATED_STATUS
from blueprints import UserMappers
from services import UserService

userService = UserService()
userMappers = UserMappers()

user_blueprint = Blueprint('user_blueprint', __name__, url_prefix = '/user')

@user_blueprint.route('/', methods = ['GET'])
def getAllUsers():
  return jsonify(userService.findAll()), HTTP_OK_STATUS

@user_blueprint.route('/<int:id>', methods = ['GET'])
def getUser(id):
  return jsonify(userService.get(id)), HTTP_OK_STATUS

@user_blueprint.route('/', methods = ['POST'])
def createUser():
  userDto = userMappers.requestToCreateUserDtoMapper(request)
  return jsonify(userService.create(userDto)), HTTP_CREATED_STATUS

@user_blueprint.route('/<int:id>', methods = ['PUT'])
def updateUser(id):
  userDto = userMappers.requestToCreateUserDtoMapper(request)
  return jsonify(userService.update(id, userDto)), HTTP_OK_STATUS

@user_blueprint.route('/<int:id>', methods = ['DELETE'])
def deleteUser(id):
  userService.delete(id)
  return '', HTTP_OK_STATUS