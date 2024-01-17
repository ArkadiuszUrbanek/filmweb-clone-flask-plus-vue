import datetime
from models import db, Review

class ReviewRepository():

  def get(self, id):
    return Review.query.get(id)

  def create(self, movieId, review):
    review.movie_id = movieId
    review.creation_date = datetime.datetime.utcnow()
    review.modification_date = datetime.datetime.utcnow()
    db.session.add(review)
    db.session.commit()
    return review

  def update(self, id, review):
    dbReview = self.get(id)
    dbReview.mark = review.mark
    dbReview.description = review.description
    dbReview.modification_date = datetime.datetime.utcnow()
    db.session.commit()
    return dbReview

  def delete(self, review):
    db.session.delete(review)
    db.session.commit()
    return