from authlib.integrations.flask_client import OAuth
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from dotenv import dotenv_values

from models import User

oauth = OAuth()

config = dotenv_values('.env')

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

bcrypt = Bcrypt()

login_manager = LoginManager()
login_manager.session_protection = 'strong'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

from .routes import auth_blueprint