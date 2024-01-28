from flask import Blueprint, jsonify, request
from controllers import HTTP_OK_STATUS, HTTP_CREATED_STATUS
from blueprints import MessageMappers
from services import MessageService

messageService = MessageService()
messageMappers = MessageMappers()

message_blueprint = Blueprint('message_blueprint', __name__, url_prefix = '/message')

@message_blueprint.route('/<int:id>', methods = ['GET'])
def getMessage(id):
  return jsonify(messageService.get(id)), HTTP_OK_STATUS

@message_blueprint.route('/<int:id>/answers', methods = ['GET'])
def getAllAnswers(id):
  return jsonify(messageService.getAllAnswers(id)), HTTP_OK_STATUS

@message_blueprint.route('/', methods = ['POST'])
def createMessage():
  messageDto = messageMappers.requestToCreateMessageDtoMapper(request)
  return jsonify(messageService.create(messageDto)), HTTP_CREATED_STATUS

@message_blueprint.route('/<parentId:id>/answer', methods = ['POST'])
def createAnswer(parentId):
  answerDto = messageMappers.requestToCreateMessageDtoMapper(request)
  return jsonify(messageService.createAnswer(parentId, answerDto)), HTTP_CREATED_STATUS

@message_blueprint.route('/<int:id>', methods = ['PUT'])
def updateMessage(id):
  messageDto = messageMappers.requestToCreateMessageDtoMapper(request)
  return jsonify(messageService.update(id, messageDto)), HTTP_OK_STATUS

@message_blueprint.route('/<int:id>', methods = ['DELETE'])
def deleteMessage(id):
  messageService.delete(id)
  return '', HTTP_OK_STATUS
