from . import db
from .utils.entity import Entity
from .utils.utcnow import utcnow

class User(db.Model, Entity):
    first_name = db.Column(db.String(20), nullable = False)
    last_name = db.Column(db.String(40), nullable = False)
    email = db.Column(db.String(40), nullable = False)
    account_type = db.Column(db.String(8), db.CheckConstraint('account_type IN (\'app\', \'facebook\', \'google\')'), nullable = False)
    #role with enum