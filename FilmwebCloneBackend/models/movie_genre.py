from . import db

movie_genre = db.Table(
    'movie_genre',
    db.metadata,
    db.Column('movie_id', db.ForeignKey('movie.id'), primary_key=True),
    db.Column('genre_id', db.ForeignKey('genre.id'), primary_key=True),
)