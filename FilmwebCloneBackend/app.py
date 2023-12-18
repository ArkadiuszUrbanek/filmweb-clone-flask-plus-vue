from flask import Flask, url_for, session
from authlib.integrations.flask_client import OAuth
from dotenv import dotenv_values
import json

app = Flask('FilmwebCloneBackend')
app.secret_key = 'very hard to guess key'

config = dotenv_values('.env')

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

app.run(host = '127.0.0.1', port = 5000, debug = True, ssl_context = ('cert.pem', 'key.pem')) #, ssl_context = 'adhoc'
