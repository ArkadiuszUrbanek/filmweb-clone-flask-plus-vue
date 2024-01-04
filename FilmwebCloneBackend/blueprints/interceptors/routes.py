from flask import Blueprint, Response, current_app, request
from flask_wtf.csrf import generate_csrf
from flask_login import current_user
from secrets import token_hex
from ..decorators import protected_funcs
from .. import csrf

interceptors_blueprint = Blueprint('interceptors_blueprint', __name__)

@interceptors_blueprint.before_app_request
def check_csrf():
    if current_user.is_authenticated or current_user.csrf_token_secret_key != None:
        current_app.config.update(WTF_CSRF_SECRET_KEY = current_user.csrf_token_secret_key)
    
    if request.endpoint != None:
        view = current_app.view_functions.get(request.endpoint)
        dest = f'{view.__module__}.{view.__name__}'
    
        if dest in protected_funcs:
            csrf.protect()

@interceptors_blueprint.after_app_request
def set_csrf_cookie(response: Response):
    current_user.csrf_token_secret_key = token_hex()
    current_app.config.update(WTF_CSRF_SECRET_KEY = current_user.csrf_token_secret_key)
    response.set_cookie(key = 'X-CSRFToken', 
                        value = generate_csrf(),
                        domain = '127.0.0.1',
                        secure = True,
                        httponly = False,
                        samesite = None)
    return response
