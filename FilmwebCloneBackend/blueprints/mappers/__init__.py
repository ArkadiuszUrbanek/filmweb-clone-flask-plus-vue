import os
from app import app
from dotenv import dotenv_values

config = dotenv_values('.env')

MOVIE_FOLDER_PATH = os.path.join(app.config['UPLOAD_FOLDER'], '/movie')
ACTOR_FOLDER_PATH = os.path.join(app.config['UPLOAD_FOLDER'], '/actor')
DIRECTOR_FOLDER_PATH = os.path.join(app.config['UPLOAD_FOLDER'], '/director')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in config['ALLOWED_EXTENSIONS']