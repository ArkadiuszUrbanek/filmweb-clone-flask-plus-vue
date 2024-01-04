from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

from .auth import oauth, auth_blueprint, bcrypt, login_manager
from .error import error_blueprint

from .decorators import protected_funcs
