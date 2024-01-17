from blueprints import MovieMappers, ReviewMappers
from dtos import CreateMovieDto, CreateReviewDto
from repositories import MovieRepository, ReviewRepository, ForumRepository, ActorRepository, DirectorRepository, GenreRepository

class MovieService():

  movieRepository = MovieRepository()
  reviewRepository = ReviewRepository()
  forumRepository = ForumRepository()
  actorRepository = ActorRepository()
  directorRepository = DirectorRepository()
  genreRepository = GenreRepository()
  movieMappers = MovieMappers()
  ReviewMappers = ReviewMappers()


def findAll(self):
  dtoTab = []
  movieTab = self.movieRepository.findAll()
  convert = lambda unit: self.forumMappers.forumSqlAlchemyToDtoMapper(unit)
  for record in movieTab:
    dtoTab.append(convert(record))
  return dtoTab

def get(self, id):
  movieDb = self.movieRepository.get(id)
  return self.movieMappers.movieSqlAlchemyToDtoMapper(movieDb)

def addReview(self, movieId, reviewDto: CreateReviewDto):
  movieDb = self.movieRepository.get(movieId)
  reviewDb = self.reviewRepository.create(movieId, self.reviewMappers.createReviewDtoToSqlAlchemyMapper(reviewDto))
  movieDb.reviews.append(reviewDb)
  return self.movieRepository.update(movieId, movieDb)

def connectForum(self, movieId, forumId):
  movieDb = self.movieRepository.get(movieId)
  forumDb = self.forumRepository.get(forumId)
  movieDb.forums.append(forumDb)
  return self.movieRepository.update(movieId, movieDb)

def connectActors(self, movieId, actorIdTab):
  movieDb = self.movieRepository.get(movieId)
  movieActors = movieDb.actors
  for id in actorIdTab:
    actorDb = self.actorRepository.get(id)
    movieActors.append(actorDb)
  movieDb.actors = movieActors
  return self.movieRepository.update(movieId, movieDb)

def connectDirectors(self, movieId, directorIdTab):
  movieDb = self.movieRepository.get(movieId)
  movieDirectors = movieDb.directors
  for id in directorIdTab:
    directorDb = self.directorRepository.get(id)
    movieDirectors.append(directorDb)
  movieDb.directors = movieDirectors
  return self.movieRepository.update(movieId, movieDb)

def connectGenres(self, movieId, genreIdTab):
  movieDb = self.movieRepository.get(movieId)
  movieGenres = movieDb.genres
  for id in genreIdTab:
    genreDb = self.genreRepository.get(id)
    movieGenres.append(genreDb)
  movieDb.gernes = movieGenres
  return self.movieRepository.update(movieId, movieDb)

def createPlainMovie(self, movieDto: CreateMovieDto):
  movieDb = self.movieMappers.createMovieDtoToSqlAlchemyMapper(movieDto)
  return self.movieRepository.create(movieDb)

def createFullMovie(self, movieDto: CreateMovieDto):
  movieDb = self.movieMappers.createMovieDtoToSqlAlchemyMapper(movieDto)
  movieDb.reviews = movieDto.reviews
  movieDb.forums = movieDto.forums
  movieDb.directors = movieDto.directors
  movieDb.actors = movieDto.actors
  movieDb.genres = movieDto.genres
  return self.movieRepository.create(movieDb)

def update(self, id, movieDto: CreateMovieDto):
  movieDb = self.movieMappers.createMovieDtoToSqlAlchemyMapper(movieDto)
  return self.movieRepository.update(id, movieDb)

def delete(self, id):
  movieDb = self.movieRepository.get(id)
  self.movieRepository.delete(movieDb)
  return