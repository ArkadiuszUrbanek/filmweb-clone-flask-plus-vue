from flask_login import AnonymousUserMixin
from enums import UserRole

class AnonymousUser(AnonymousUserMixin):
    role = UserRole.GUEST
    csrf_token_secret_key = None