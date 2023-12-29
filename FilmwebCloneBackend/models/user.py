from . import db
from .blueprints.entity import Entity
from .utils import utcnow
from enums.UserRoleEnum import UserRole
from flask_login import UserMixin

class User(db.Model,Entity, UserMixin):
    first_name = db.Column(db.String(20), nullable = False)
    last_name = db.Column(db.String(40), nullable = False)
    email = db.Column(db.String(40), nullable = False)
    password_hash = db.Column(db.String, nullable = False)
    account_type = db.Column(db.String(8), db.CheckConstraint('account_type IN (\'app\', \'facebook\', \'google\')'), nullable = False)
    role = db.Column(db.Enum(UserRole), nullable = False)

    forum_id = db.Column(db.Integer, db.ForeignKey('forum.id'), nullable = True)
    forums = db.relationship('Forum', back_populates='author', cascade = 'all, delete')
    message_id = db.Column(db.Integer, db.ForeignKey('message.id'), nullable = True)
    messages = db.relationship('Message', back_populates='author', cascade = 'all, delete')
    review_id = db.Column(db.Integer, db.ForeignKey('review.id'), nullable = True)
    reviews = db.relationship('Review', back_populates='author')
