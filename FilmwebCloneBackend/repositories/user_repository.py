import datetime
from models import db, User

class UserRepository():

  def findAll(self):
    return User.query.order_by(User.id).all()

  def get(self, id):
    return User.query.get(id)

  def create(self, user):
    user.creation_date = datetime.datetime.utcnow()
    user.modification_date = datetime.datetime.utcnow()
    db.session.add(user)
    db.session.commit()
    return user

  def update(self, id, user):
    dbUser = self.get(id)
    dbUser.first_name = user.first_name
    dbUser.last_name = user.last_name
    dbUser.email = user.email
    dbUser.gender = user.gender
    dbUser.password_hash = user.password_hash
    dbUser.account_type = user.account_type
    dbUser.role = user.role
    dbUser.modification_date = datetime.datetime.utcnow()
    db.session.commit()
    return dbUser

  def delete(self, user):
    db.session.delete(user)
    db.session.commit()
    return