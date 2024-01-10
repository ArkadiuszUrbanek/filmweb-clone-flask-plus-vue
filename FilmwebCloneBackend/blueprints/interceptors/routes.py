from flask import Blueprint, Response, current_app, request, session, g
from flask_wtf.csrf import generate_csrf, validate_csrf
from wtforms import ValidationError
from werkzeug.exceptions import BadRequest
from secrets import token_hex
from ..decorators import protected_endpoints
from .utils import same_origin

interceptors_blueprint = Blueprint('interceptors_blueprint', __name__)

@interceptors_blueprint.before_app_request
def check_csrf():
    if request.endpoint is None:
        return
    
    if request.method not in current_app.config['WTF_CSRF_METHODS']:
        return

    if request.is_secure and current_app.config['WTF_CSRF_SSL_STRICT']:
        if not request.referrer:
            raise BadRequest(description = 'The referrer header is missing.')

        good_referrer = f'https://{request.host}/'

        if not same_origin(request.referrer, good_referrer):
            raise BadRequest(description = 'The referrer does not match the host.')

    view = current_app.view_functions.get(request.endpoint)
    destination_endpoint = f'{view.__module__}.{view.__name__}'
    
    if destination_endpoint not in protected_endpoints:
        return
    
    csrf_headers = current_app.config.get('WTF_CSRF_HEADERS', [])
    csrf_token = next((request.headers.get(header) for header in csrf_headers if request.headers.get(header)), None)

    try:
        validate_csrf(data = csrf_token,
                      secret_key = session.get('csrf_token_secret_key', None),
                      token_key = current_app.config.get('WTF_CSRF_FIELD_NAME', 'csrf_token'))
        
    except ValidationError as e:
        raise BadRequest(description = e.args[0])

    g.csrf_valid = True

@interceptors_blueprint.after_app_request
def set_csrf_cookie(response: Response):
    csrf_token_secret_key = token_hex()
    session['csrf_token_secret_key'] = csrf_token_secret_key
    response.set_cookie(key = 'X-CSRFToken', 
                        value = generate_csrf(secret_key = csrf_token_secret_key),
                        domain = '127.0.0.1',
                        secure = True,
                        httponly = False,
                        samesite = None)
    return response
