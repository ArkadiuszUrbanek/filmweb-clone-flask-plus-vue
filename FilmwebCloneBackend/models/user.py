from . import db
from .utils.entity import Entity
from Enums.UserRoleEnum import UserRole

class User(db.Model, Entity):
    first_name = db.Column(db.String(20), nullable = False)
    last_name = db.Column(db.String(40), nullable = False)
    email = db.Column(db.String(40), nullable = False)
    account_type = db.Column(db.String(8), db.CheckConstraint('account_type IN (\'app\', \'facebook\', \'google\')'), nullable = False)
    role = db.Column(db.Enum(UserRole), nullable = False)

    forum_id = db.Column(db.Integer, db.ForeignKey("forum.id"), nullable = True)
    forums = db.relationship("Forum", back_populates="user")

    message_id = db.Column(db.Integer, db.ForeignKey("message.id"), nullable = True)
    messages = db.relationship("Message", back_populates="user")

    review_id = db.Column(db.Integer, db.ForeignKey("review.id"), nullable = True)
    reviews = db.relationship("Review", back_populates="user")