import datetime
from sqlalchemy import select
from models import db
from models.user import User

class UserRepository():

  def findAll():
    return db.session.execute(select(User).orderBy(User.id))

  def get(id: int):
    return db.session.execute(select(User).where(User.id == id))

  def create(user: User):
    user.creation_date = datetime.datetime.utcnow()
    user.modification_date = datetime.datetime.utcnow()
    db.session.add(user)
    db.session.commit()
    return user

  def update(id, user: User):
    dbUser: User = db.session.execute(select(User).where(User.id == id))
    dbUser.first_name = user.first_name
    dbUser.last_name = user.last_name
    dbUser.email = user.email
    dbUser.password_hash = user.password_hash
    dbUser.account_type = user.account_type
    dbUser.role = user.role
    dbUser.modification_date = datetime.datetime.utcnow()
    db.session.commit()
    return dbUser

  def delete(user: User):
    db.session.delete(user)
    db.session.commit()
    return