from flask import Blueprint, Response
from flask_wtf.csrf import CSRFError
from werkzeug.exceptions import NotFound, Unauthorized, Forbidden
from http import HTTPStatus

error_blueprint = Blueprint('error_blueprint', __name__)

@error_blueprint.app_errorhandler(CSRFError)
def handle_csrf_error(e):
    return Response(response = e.description, status = HTTPStatus.BAD_REQUEST, content_type = 'text/plain')

@error_blueprint.app_errorhandler(NotFound)
def handle_not_found(e):
    return Response(response = e.description, status = HTTPStatus.NOT_FOUND, content_type = 'text/plain')

@error_blueprint.app_errorhandler(Unauthorized)
def handle_unauthorized(e):
    return Response(response = e.description, status = HTTPStatus.UNAUTHORIZED, content_type = 'text/plain')

@error_blueprint.app_errorhandler(Forbidden)
def handle_forbidden(e):
    return Response(response = e.description, status = HTTPStatus.FORBIDDEN, content_type = 'text/plain')