from flask import Response
from flask_login import current_user
from functools import wraps
from http import HTTPStatus

def roles_required(*roles):
    def decorator(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            if current_user.role not in roles:
                return Response(response = 'The current role does not allow the request to be processed.', 
                                status = HTTPStatus.FORBIDDEN, 
                                content_type = 'text/plain')

            return func(*args, **kwargs)
        return wrapped
    return decorator