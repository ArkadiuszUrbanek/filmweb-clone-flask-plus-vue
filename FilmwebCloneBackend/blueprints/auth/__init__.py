from flask import session
from flask_oauthlib.client import OAuth
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from itsdangerous import URLSafeTimedSerializer
from models import User, AnonymousUser
from werkzeug.exceptions import Unauthorized
from dotenv import dotenv_values

config = dotenv_values('.env')

oauth = OAuth()

google = oauth.remote_app(
    name = 'google',
    consumer_key = config['GOOGLE_OAUTH2_CLIENT_ID'],
    consumer_secret = config['GOOGLE_OAUTH2_SECRET_KEY'],
    request_token_params =  {'scope': 'openid email profile'},
    base_url = 'https://www.googleapis.com/oauth2/v1/',
    request_token_url = None,
    access_token_method = 'POST',
    access_token_url = 'https://accounts.google.com/o/oauth2/token',
    authorize_url = 'https://accounts.google.com/o/oauth2/auth'
)

@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')

facebook = oauth.remote_app(
    name = 'facebook',
    consumer_key = config['FACEBOOK_OAUTH2_CLIENT_ID'],
    consumer_secret = config['FACEBOOK_OAUTH2_SECRET_KEY'],
    request_token_params =  {'scope': 'email public_profile'},
    base_url = 'https://graph.facebook.com',
    request_token_url = None,
    access_token_method = 'GET',
    access_token_url = '/oauth/access_token',
    authorize_url = 'https://www.facebook.com/dialog/oauth'
)

@facebook.tokengetter
def get_facebook_oauth_token():
    return session.get('facebook_token')

bcrypt = Bcrypt()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.anonymous_user = AnonymousUser

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@login_manager.unauthorized_handler
def unauthorized_callback():
    raise Unauthorized(description = 'Login is required.')

mail = Mail()

url_safe_token_generator = URLSafeTimedSerializer(secret_key = config['URL_SAFE_TOKEN_GENERATOR_SECRET_KEY'])

from .routes import auth_blueprint