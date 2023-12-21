from flask import Flask, url_for
from models import db, User
from authlib.integrations.flask_client import OAuth
import dotenv
import json

#Pobranie danych konfiguracyjnych z pliku .env
config = dotenv.dotenv_values('.env')

app = Flask(__name__)
app.config["SECRET_KEY"] = 'very hard to guess key'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{config["MYSQL_USERNAME"]}:{config["MYSQL_PASSWORD"]}@localhost/{config["MYSQL_DATABASE_NAME"]}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

oauth = OAuth(app)

google = oauth.register(name = 'google',
                        client_id = config['GOOGLE_OAUTH2_CLIENT_ID'],
                        client_secret = config['GOOGLE_OAUTH2_SECRET_KEY'],
                        server_metadata_url = 'https://accounts.google.com/.well-known/openid-configuration',
                        client_kwargs = {
                            'scope': 'openid email profile'              
                        })

facebook = oauth.register(name = 'facebook',
                          client_id = config['FACEBOOK_OAUTH2_CLIENT_ID'],
                          client_secret = config['FACEBOOK_OAUTH2_SECRET_KEY'],
                          api_base_url = 'https://graph.facebook.com/v18.0/',
                          access_token_url = 'https://graph.facebook.com/v18.0/oauth/access_token',
                          authorize_url = 'https://www.facebook.com/v18.0/dialog/oauth',
                          userinfo_endpoint = 'me?fields=id,first_name,last_name,email',
                          client_kwargs = {
                              'scope': 'email public_profile'              
                          })

@app.route('/register')
def register():
    return

@app.route('/login')
def login():
    return

@app.route('/login/facebook')
def requestFacebookLogin():
    facebook = oauth.create_client('facebook')
    return facebook.authorize_redirect(redirect_uri = url_for('facebookCallback', _external = True))

@app.route('/login/google')
def requestGoogleLogin():
    google = oauth.create_client('google')
    return google.authorize_redirect(redirect_uri = url_for('googleCallback', _external = True))

@app.route('/login/facebook/callback')
def facebookCallback():
    facebook = oauth.create_client('facebook')
    response = facebook.authorize_access_token()
    return json.dumps(response)

@app.route('/login/google/callback')
def googleCallback():
    google = oauth.create_client('google')
    response = google.authorize_access_token()
    return json.dumps(response)

if __name__ == "__main__":
    with app.app_context(): 
        db.create_all()
        
    app.run(host = '127.0.0.1', port = 5000, debug = True, ssl_context = 'adhoc')
