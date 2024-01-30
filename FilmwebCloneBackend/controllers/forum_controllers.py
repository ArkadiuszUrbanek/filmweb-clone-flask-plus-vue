from flask import Blueprint, jsonify, request
from controllers import HTTP_OK_STATUS, HTTP_CREATED_STATUS
from blueprints import ForumMappers, MessageMappers
from services import ForumService

forumService = ForumService()
forumMappers = ForumMappers()
messageMappers = MessageMappers()

forum_blueprint = Blueprint('forum_blueprint', __name__, url_prefix = '/forum')

@forum_blueprint.route('/', methods = ['GET'])
def getAllForums():
  return jsonify(forumService.findAll()), HTTP_OK_STATUS

@forum_blueprint.route('/<int:id>', methods = ['GET'])
def getForum(id):
  return jsonify(forumService.get(id)), HTTP_OK_STATUS

@forum_blueprint.route('/message', methods = ['POST'])
def addMessage():
  messageDto = messageMappers.requestToCreateMessageDtoMapper(request)
  return jsonify(forumService.addMessage(messageDto)), HTTP_CREATED_STATUS

@forum_blueprint.route('/', methods = ['POST'])
def createForum():
  forumDto = forumMappers.requestToCreateForumDtoMapper(request)
  return jsonify(forumService.create(forumDto)), HTTP_CREATED_STATUS

@forum_blueprint.route('/<int:id>', methods = ['PUT'])
def updateForum(id):
  forumDto = forumMappers.requestToCreateForumDtoMapper(request)
  return jsonify(forumService.update(id, forumDto)), HTTP_OK_STATUS

@forum_blueprint.route('/<int:id>', methods = ['DELETE'])
def deleteForum(id):
  forumService.delete(id)
  return '', HTTP_OK_STATUS