from flask_login import AnonymousUserMixin
from enums import UserRole

class AnonymousUser(AnonymousUserMixin):
    role = UserRole.GUEST