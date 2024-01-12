from dtos import MovieDto, CreateMovieDto
from models import Movie

class MovieMappers():
  def movieSqlAlchemyToDtoMapper(self, movieDb: Movie) -> MovieDto:
    movieDto = MovieDto()
    movieDto.id = movieDb.id
    movieDto.title = movieDb.title
    movieDto.premiere_date = movieDb.premiere_date
    movieDto.length_time = movieDb.length_time
    movieDto.description = movieDb.description
    movieDto.reviews = movieDb.reviews
    movieDto.forums = movieDb.forums
    movieDto.directors = movieDb.directors
    movieDto.actors = movieDb.actors
    movieDto.genres = movieDb.genres
    return movieDto

  def createMovieDtoToSqlAlchemyMapper(self, createMovieDto: CreateMovieDto) -> Movie:
    return Movie(createMovieDto.title, createMovieDto.premiere_date, createMovieDto.length_time, createMovieDto.description)