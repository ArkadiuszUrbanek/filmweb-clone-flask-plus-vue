from dtos import CreateMovieDto
from repositories import MovieRepository

#   def createWithAllDetails(self, movie, directorsTab, actorsTab, genresTab):
#     dbMovie = self.create(movie)
#     dbMovie.directors = directorsTab
#     dbMovie.actors = actorsTab
#     dbMovie.genres = genresTab
#     db.session.add(dbMovie)
#     db.session.commit()
#     return dbMovie

class MovieService():

  movieRepository = MovieRepository()