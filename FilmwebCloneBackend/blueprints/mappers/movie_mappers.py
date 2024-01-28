from flask import Request
from dtos import MovieDto, CreateMovieDto
from models import Movie

class MovieMappers():

  def requestToCreateMovieDtoMapper(self, request: Request) -> CreateMovieDto:
    createMovieDto = CreateMovieDto()
    createMovieDto.title = request.json.get('title') if request.json.get('title') != None else ''
    createMovieDto.premiere_date = request.json.get('premiere_date')
    createMovieDto.length_time = request.json.get('length_time') if request.json.get('length_time') != None else 0
    createMovieDto.description = request.json.get('description') if request.json.get('descirption') != None else ''
    createMovieDto.reviews = request.json.get('reviews') if request.json.get('reviews') != None else []
    createMovieDto.forums = request.json.get('forums') if request.json.get('forums') != None else []
    createMovieDto.directors = request.json.get('directors') if request.json.get('directors') != None else []
    createMovieDto.actors = request.json.get('actors') if request.json.get('actors') != None else []
    createMovieDto.genres = request.json.get('genres') if request.json.get('genres') != None else []
    return createMovieDto

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