from flask import Flask, url_for, session
from authlib.integrations.flask_client import OAuth
from dotenv import dotenv_values

app = Flask('FilmwebCloneBackend')
app.secret_key = 'very hard to guess key'

oauth = OAuth(app)

config = dotenv_values('.env')
google = oauth.register(name = 'google',
                        client_id = config['GOOGLE_OAUTH2_CLIENT_ID'],
                        client_secret = config['GOOGLE_OAUTH2_SECRET_KEY'],
                        server_metadata_url = 'https://accounts.google.com/.well-known/openid-configuration',
                        #access_token_url = 'https://accounts.google.com/o/oauth2/token',
                        #access_token_url = 'https://oauth2.googleapis.com/token',
                        #access_token_params = None,
                        #authorize_url = 'https://accounts.google.com/o/oauth2/auth',
                        #authorize_url = 'https://accounts.google.com/o/oauth2/v2/auth',
                        #authorize_params = None,
                        #api_base_url = 'https://www.googleapis.com/oauth2/v1/',
                        #userinfo_endpoint = 'https://openidconnect.googleapis.com/v1/userinfo',
                        #userinfo_endpoint = 'https://openidconnect.googleapis.com/v1/userinfo',
                        client_kwargs = { 
                            'scope': 'openid email profile', 
                            #'redirect_url': 'http://localhost:5000/login/google/callback'                 
                        })

@app.route('/')
def index():
    return 'hello'

@app.route('/login/google')
def requestGoogleLogin():
    google = oauth.create_client('google')
    return google.authorize_redirect(redirect_uri = url_for('googleCallback', external = True))

@app.route('/login/google/callback')
def googleCallback():
    google = oauth.create_client('google')
    token = google.authorize_access_token()
    response = google.get('userinfo', token = token)
    userInfo = response.json()
    print(userInfo)

app.run(host = '127.0.0.1', port = 5000, debug = True)
