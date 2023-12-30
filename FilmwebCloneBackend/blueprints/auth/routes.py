from flask import Blueprint, url_for, request
from flask_login import login_user, logout_user, login_required
from . import oauth, bcrypt
from models import db, User
from enums import UserRole, UserAccountType
import json

auth_blueprint = Blueprint('auth_blueprint', __name__, url_prefix = '/auth')

@auth_blueprint.route('/register', methods = ['POST'])
def register():
    hashed_password = bcrypt.generate_password_hash(request.args.get('password'))
    db.session.add(
        User(
            first_name = request.args.get('first_name'),
            last_name = request.args.get('last_name'),
            email = request.args.get('email'),
            password_hash = hashed_password,
            account_type = UserAccountType.APP,
            role = UserRole.USER
        )
    )
    db.session.commit()
    return

@auth_blueprint.route('/login', methods = ['POST'])
def login():
    user = User.query.filter_by(email = request.args.get('email')).first()
    if user is not None and bcrypt.check_password_hash(user.password_hash, request.args.get('password')):
        login_user(user)
        return
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

@auth_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    return