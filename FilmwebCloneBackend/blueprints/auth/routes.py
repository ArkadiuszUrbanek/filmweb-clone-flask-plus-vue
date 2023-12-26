from flask import Blueprint, url_for
from . import oauth
import json

auth_blueprint = Blueprint('auth_blueprint', __name__) #,  url_prefix = '/auth'

@auth_blueprint.route('/register')
def register():
    return

@auth_blueprint.route('/login')
def login():
    return

@auth_blueprint.route('/login/facebook')
def requestFacebookLogin():
    facebook = oauth.create_client('facebook')
    return facebook.authorize_redirect(redirect_uri = url_for('auth_blueprint.facebookCallback', _external = True))

@auth_blueprint.route('/login/google')
def requestGoogleLogin():
    google = oauth.create_client('google')
    return google.authorize_redirect(redirect_uri = url_for('auth_blueprint.googleCallback', _external = True))

@auth_blueprint.route('/login/facebook/callback')
def facebookCallback():
    facebook = oauth.create_client('facebook')
    response = facebook.authorize_access_token()
    return json.dumps(response)

@auth_blueprint.route('/login/google/callback')
def googleCallback():
    google = oauth.create_client('google')
    response = google.authorize_access_token()
    return json.dumps(response)