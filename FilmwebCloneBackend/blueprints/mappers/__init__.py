from dotenv import dotenv_values

config = dotenv_values('.env')

MOVIE_FOLDER_PATH = config['UPLOAD_FOLDER_DIRECTORY'] + '\\movie'
ACTOR_FOLDER_PATH = config['UPLOAD_FOLDER_DIRECTORY'] + '\\actor'
DIRECTOR_FOLDER_PATH = config['UPLOAD_FOLDER_DIRECTORY'] + '\\director'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in config['ALLOWED_EXTENSIONS']