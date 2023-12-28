from . import db
from .utils.entity import Entity
from .utils.utcnow import utcnow

class Movie(db.Model, Entity):
  title = db.Column(db.String(100), nullable=False)
  premiere_date = db.Column(db.DateTime, nullable=True, server_default = utcnow())
  length_time = db.Column(db.Integer, nullable=True)
  description = db.Column(db.String(10000), nullable=True)

  review_id = db.Column(db.Integer, db.ForeignKey("review.id"), nullable = True)
  reviews = db.relationship("Review", back_populates="movie")

  forum_id = db.Column(db.Integer, db.ForeignKey("forum.id"), nullable = True)
  forums = db.relationship("Forum", back_populates="movie")