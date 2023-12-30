from flask import Response
from flask_login import current_user
from functools import wraps
from http import HTTPStatus

def roles_required(*roles):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            if not current_user.is_authenticated:
                return Response(status = HTTPStatus.UNAUTHORIZED)

            if current_user.role not in roles:
                return Response(status = HTTPStatus.FORBIDDEN)

            return fn(*args, **kwargs)

        return decorator
    return wrapper