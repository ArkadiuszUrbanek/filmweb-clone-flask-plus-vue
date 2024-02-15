from flask import Blueprint, Response
from werkzeug.exceptions import BadRequest, NotFound, Unauthorized, Forbidden, InternalServerError, Gone
from http import HTTPStatus

errors_blueprint = Blueprint('errors_blueprint', __name__)

@errors_blueprint.app_errorhandler(BadRequest)
def handle_400_bad_request(exception):
    return Response(response = exception.description, status = HTTPStatus.BAD_REQUEST, content_type = 'text/plain')

@errors_blueprint.app_errorhandler(Unauthorized)
def handle_401_unauthorized(exception):
    return Response(response = exception.description, status = HTTPStatus.UNAUTHORIZED, content_type = 'text/plain')

@errors_blueprint.app_errorhandler(Forbidden)
def handle_403_forbidden(exception):
    return Response(response = exception.description, status = HTTPStatus.FORBIDDEN, content_type = 'text/plain')

@errors_blueprint.app_errorhandler(NotFound)
def handle_404_not_found(exception):
    return Response(response = exception.description, status = HTTPStatus.NOT_FOUND, content_type = 'text/plain')

@errors_blueprint.app_errorhandler(Gone)
def handle_410_gone(exception):
    return Response(response = exception.description, status = HTTPStatus.GONE, content_type = 'text/plain')

@errors_blueprint.app_errorhandler(InternalServerError)
def handle_500_internal_server_error(exception):
    return Response(response = exception.description, status = HTTPStatus.INTERNAL_SERVER_ERROR, content_type = 'text/plain')