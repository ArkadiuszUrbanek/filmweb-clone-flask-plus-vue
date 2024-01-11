import datetime
from models import db, Forum

class ForumRepository():

  def findAll(self):
    return Forum.query.order_by(Forum.id).all()

  def get(self, id):
    return Forum.query.get(id)

  def create(self, forum):
    forum.creation_date = datetime.datetime.utcnow()
    forum.modification_date = datetime.datetime.utcnow()
    db.session.add(forum)
    db.session.commit()
    return forum

  def update(self, id, forum):
    dbForum = self.get(id)
    dbForum.name = forum.name
    dbForum.description = forum.description
    dbForum.tags = forum.tags
    dbForum.messages = forum.messages
    dbForum.user_id = forum.user_id
    dbForum.movie_id = forum.movie_id
    dbForum.modification_date = datetime.datetime.utcnow()
    db.session.commit()
    return dbForum

  def delete(self, forum):
    db.session.delete(forum)
    db.session.commit()
    return