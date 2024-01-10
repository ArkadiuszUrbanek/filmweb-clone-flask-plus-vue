from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

from .auth import oauth, auth_blueprint, bcrypt, login_manager
from .errors import errors_blueprint
from .interceptors import interceptors_blueprint
from .mappers.user_mappers import UserMappers
from .mappers.message_mappers import MessageMappers
from .mappers.forum_mappers import ForumMappers
