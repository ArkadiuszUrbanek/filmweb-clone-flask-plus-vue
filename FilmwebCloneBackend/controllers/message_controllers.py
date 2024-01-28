from flask import Blueprint, jsonify, request
from controllers import HTTP_OK_STATUS, HTTP_CREATED_STATUS
from blueprints import MessageMappers
from services import MessageService

messageService = MessageService()
messageMappers = MessageMappers()

message_blueprint = Blueprint('message_blueprint', __name__, url_prefix = '/message')