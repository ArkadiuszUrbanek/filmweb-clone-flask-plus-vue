HTTP_OK_STATUS = 200
HTTP_CREATED_STATUS = 201

from .user_controllers import user_blueprint
from .review_controllers import review_blueprint
from .movie_controllers import movie_blueprint
from .message_controllers import message_blueprint