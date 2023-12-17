from flask import Flask, url_for, session
from authlib.integrations.flask_client import OAuth
from dotenv import dotenv_values
import json

app = Flask('FilmwebCloneBackend')
app.secret_key = 'very hard to guess key'

oauth = OAuth(app)

config = dotenv_values('.env')
google = oauth.register(name = 'google',
                        client_id = config['GOOGLE_OAUTH2_CLIENT_ID'],
                        client_secret = config['GOOGLE_OAUTH2_SECRET_KEY'],
                        server_metadata_url = 'https://accounts.google.com/.well-known/openid-configuration',
                        client_kwargs = { 
                            'scope': 'openid email profile'              
                        })

@app.route('/login/google')
def requestGoogleLogin():
    google = oauth.create_client('google')
    return google.authorize_redirect(redirect_uri = url_for('googleCallback', _external = True))

@app.route('/login/google/callback')
def googleCallback():
    google = oauth.create_client('google')
    response = google.authorize_access_token()
    return json.dumps(response)

app.run(host = '127.0.0.1', port = 5000, debug = True)
