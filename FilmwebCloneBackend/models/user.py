from . import db
from .utils.entity import Entity
from Enums.UserRoleEnum import UserRole

class User(db.Model, Entity):
    first_name = db.Column(db.String(20), nullable = False)
    last_name = db.Column(db.String(40), nullable = False)
    email = db.Column(db.String(40), nullable = False)
    account_type = db.Column(db.String(8), db.CheckConstraint('account_type IN (\'app\', \'facebook\', \'google\')'), nullable = False)
    role = db.Column(db.Enum(UserRole), nullable = False)