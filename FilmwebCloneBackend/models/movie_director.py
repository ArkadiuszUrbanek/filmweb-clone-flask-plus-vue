from . import db

movie_director = db.Table(
    "movie_director",
    db.metadata,
    db.Column("movie_id", db.ForeignKey("movie.id"), primary_key=True),
    db.Column("director_id", db.ForeignKey("director.id"), primary_key=True),
)