import os
import json
from flask import Request
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
    jsonForm = json.loads(request.form.get('data'))
    createMovieDto = CreateMovieDto()
    createMovieDto.title = jsonForm.get('title') if jsonForm.get('title') != None else ''
    createMovieDto.premiere_date = jsonForm.get('premiere_date')
    createMovieDto.length_time =jsonForm.get('length_time') if jsonForm.get('length_time') != None else 0
    createMovieDto.description = jsonForm.get('description') if jsonForm.get('description') != None else ''
    createMovieDto.reviews = jsonForm.get('reviews') if jsonForm.get('reviews') != None else []
    createMovieDto.forums = jsonForm.get('forums') if jsonForm.get('forums') != None else []
    createMovieDto.directors = jsonForm.get('directors') if jsonForm.get('directors') != None else []
    createMovieDto.actors = jsonForm.get('actors') if jsonForm.get('actors') != None else []
    createMovieDto.genres = jsonForm.get('genres') if jsonForm.get('genres') != None else []
    if 'file' in request.files:
        print('there is file')
        file = request.files['file']
        if file and file.filename != '' and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print(filename)
            print(MOVIE_FOLDER_PATH)
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