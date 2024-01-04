from functools import wraps

protected_funcs = set()

def csrf_token_required(func):
    view_location = '.'.join((func.__module__, func.__name__))
    protected_funcs.add(view_location)
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper