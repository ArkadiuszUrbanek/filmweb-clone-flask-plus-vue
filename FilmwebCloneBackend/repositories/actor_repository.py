import datetime
from models import db, Actor

class ActorRepository():

  def findAll(self):
    return Actor.query.order_by(Actor.last_name).all()

  def get(self, id):
    return Actor.query.get(id)

  def create(self, actor):
    actor.create_date = datetime.datetime.utcnow()
    actor.modification_date = datetime.datetime.utcnow()
    db.session.add(actor)
    db.session.commit()
    return actor

  def update(self, id, actor):
    dbActor = self.get(id)
    dbActor.first_name = actor.first_name
    dbActor.last_name = actor.last_name
    dbActor.nationality = actor.nationality
    dbActor.description = actor.description
    dbActor.modification_date = datetime.datetime.utcnow()
    db.session.commit()
    return dbActor

  def delete(self, actor):
    db.session.delete(actor)
    db.session.commit()
    return