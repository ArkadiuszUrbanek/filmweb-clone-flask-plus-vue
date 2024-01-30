HTTP_OK_STATUS = 200
HTTP_CREATED_STATUS = 201

from .user_controllers import user_blueprint
from .review_controllers import review_blueprint
from .movie_controllers import movie_blueprint
from .message_controllers import message_blueprint
from .genre_controllers import genre_blueprint
from .forum_controllers import forum_blueprint
from .director_controllers import director_blueprint
from .actor_controllers import actor_blueprint