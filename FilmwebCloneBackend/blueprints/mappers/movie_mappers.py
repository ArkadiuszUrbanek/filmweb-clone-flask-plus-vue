import os
from flask import Request, send_from_directory
from werkzeug.utils import secure_filename
from blueprints.mappers import allowed_file, MOVIE_FOLDER_PATH
from dtos import MovieDto, CreateMovieDto
from models import Movie

from .review_mappers import ReviewMappers
from .forum_mappers import ForumMappers
from .director_mappers import DirectorMappers
from .actor_mappers import ActorMappers
from .genre_mappers import GenreMappers

class MovieMappers():
  def requestToCreateMovieDtoMapper(self, request: Request) -> CreateMovieDto:
    createMovieDto = CreateMovieDto()
    createMovieDto.title = request.json.get('title') if request.json.get('title') != None else ''
    createMovieDto.premiere_date = request.json.get('premiere_date')
    createMovieDto.length_time = request.json.get('length_time') if request.json.get('length_time') != None else 0
    createMovieDto.description = request.json.get('description') if request.json.get('description') != None else ''
    createMovieDto.reviews = request.json.get('reviews') if request.json.get('reviews') != None else []
    createMovieDto.forums = request.json.get('forums') if request.json.get('forums') != None else []
    createMovieDto.directors = request.json.get('directors') if request.json.get('directors') != None else []
    createMovieDto.actors = request.json.get('actors') if request.json.get('actors') != None else []
    createMovieDto.genres = request.json.get('genres') if request.json.get('genres') != None else []
    if 'file' in request.files:
        print('there is file')
        file = request.files['file']
        if file and file.filename != '' and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print(filename)
            file.save(os.path.join(MOVIE_FOLDER_PATH, filename))
            createMovieDto.file_path = filename
    return createMovieDto

  def movieSqlAlchemyToDtoMapper(self, movieDb: Movie) -> MovieDto:
    reviewMappers = ReviewMappers()
    forumMappers = ForumMappers()
    directorMappers = DirectorMappers()
    actorMappers = ActorMappers()
    genreMappers = GenreMappers()
    movieDto = MovieDto()
    movieDto.id = movieDb.id
    movieDto.title = movieDb.title
    movieDto.premiere_date = movieDb.premiere_date
    movieDto.length_time = movieDb.length_time
    movieDto.file_path = send_from_directory(movieDb.file_path)
    movieDto.description = movieDb.description
    movieDto.reviews = []
    for review in movieDb.reviews:
        movieDto.reviews.append(reviewMappers.reviewSqlAlchemyToDtoMapper(review))
    movieDto.forums = []
    for forum in movieDb.forums:
      movieDto.forums.append(forumMappers.forumSqlAlchemyToDtoMapper(forum))
    movieDto.directors = []
    for director in movieDb.directors:
       movieDto.directors.append(directorMappers.directorSqlAlchemyToDtoMapper(director))
    movieDto.actors = []
    for actor in movieDb.actors:
       movieDto.actors.append(actorMappers.actorSqlAlchemyToDtoMapper(actor))
    movieDto.genres = []
    for genre in movieDb.genres:
        movieDto.genres.append(genreMappers.genreSqlAlchemyToDtoMapper(genre))
    return movieDto

  def createMovieDtoToSqlAlchemyMapper(self, createMovieDto: CreateMovieDto) -> Movie:
    return Movie(createMovieDto.title, createMovieDto.premiere_date, createMovieDto.length_time, createMovieDto.file_path, createMovieDto.description)