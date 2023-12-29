from . import db

movie_actor = db.Table(
    "movie_actor",
    db.metadata,
    db.Column("movie_id", db.ForeignKey("movie.id"), primary_key=True),
    db.Column("actor_id", db.ForeignKey("actor.id"), primary_key=True),
)