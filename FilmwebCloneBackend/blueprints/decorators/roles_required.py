from flask_login import current_user
from functools import wraps
from werkzeug.exceptions import Forbidden

def roles_required(*roles):
    def decorator(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            if current_user.role not in roles:
                raise Forbidden(description = 'The current role does not allow the request to be processed.')

            return func(*args, **kwargs)
        return wrapped
    return decorator