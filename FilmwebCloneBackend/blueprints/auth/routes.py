from flask import Blueprint, url_for, request, Response, session, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from flask_mail import Message
from sqlalchemy import and_
from sqlalchemy.orm.exc import MultipleResultsFound
from flask_oauthlib.client import OAuthException
from . import bcrypt, facebook, google, mail, url_safe_token_generator
from ..decorators import csrf_token_required
from models import db, User
from enums import UserRole, UserAccountType
from http import HTTPStatus
from werkzeug.exceptions import InternalServerError, Unauthorized, BadRequest, Gone
from itsdangerous import SignatureExpired
from secrets import token_hex
from app import config
from dotenv import dotenv_values

config = dotenv_values('.env')

auth_blueprint = Blueprint('auth_blueprint', __name__, url_prefix = '/auth')

@auth_blueprint.route('/register', methods = ['POST'])
def register():
    email = request.args.get('email')

    db.session.add(
        User(
            first_name = request.args.get('first_name'),
            last_name = request.args.get('last_name'),
            email = email,
            email_confirmed = False,
            password_hash = bcrypt.generate_password_hash(request.args.get('password')),
            account_type = UserAccountType.APP,
            role = UserRole.USER
        )
    )
    db.session.commit()

    email_message = Message(
        subject = 'Email confirmation link',
        sender = config['MAIL_USERNAME'],
        recipients = [email]
    )

    salt = token_hex(10)
    session['url_safe_token_generator_salt'] = salt # Gdzieś trzeba przechowywać sól. Nawet dla niezalogowanego użytkownika, lecz wpisanego już do bazy!!!

    email_confirmation_link = url_for(
        endpoint = 'auth_blueprint.confirmEmail',
        token = url_safe_token_generator.dumps(obj = email, salt = salt),
        _external = True
    )

    email_message.body = f'Click to activate your account -> {email_confirmation_link}'

    mail.send(email_message)

    return Response(status = HTTPStatus.CREATED)

@auth_blueprint.route('/email/confirm/<token>', methods = ['PATCH'])
def confirmEmail(token):
    salt = session.get('url_safe_token_generator_salt', None) # pobranie soli, ale nie wiemy jaki użytkownik o nią prosi

    if salt is None: # Jeżeli nie ma soli. Albo bardziej jeżeli nie ma aktywnej soli...
        raise InternalServerError(description = 'The data cannot be reconstructed from the token.')

    session.pop('url_safe_token_generator_salt')

    try:
        email = url_safe_token_generator.loads(s = token, max_age = 60 * 60 * 24, salt = salt)

    except SignatureExpired as e:
        raise Gone(description = e.message)

    updated_rows_count = User.query \
        .filter(and_(User.email == email, User.account_type == UserAccountType.APP, User.email_confirmed == False)) \
        .update({'email_confirmed': True})
    db.session.commit()

    if updated_rows_count == 0:
        raise Unauthorized(description = 'Email address has been already confirmed.')

    return Response(status = HTTPStatus.NO_CONTENT)

@auth_blueprint.route('/email/confirmation-link', methods = ['POST'])
def resendEmailConfirmationLink():
    email = request.args.get('email')

    email_message = Message(
        subject = 'Email confirmation link',
        sender = config['MAIL_USERNAME'],
        recipients = [email]
    )

    salt = token_hex(10)
    session['url_safe_token_generator_salt'] = salt

    email_confirmation_link = url_for(
        endpoint = 'auth_blueprint.confirmEmail',
        token = url_safe_token_generator.dumps(obj = email, salt = salt),
        _external = True
    )

    email_message.body = f'Click to activate your account -> {email_confirmation_link}'

    mail.send(email_message)

    return Response(status = HTTPStatus.NO_CONTENT)

@auth_blueprint.route('/login', methods = ['POST'])
def login():
    if current_user.is_authenticated:
        raise Unauthorized(description = 'You need to log out first.')
    
    try:
        user = User.query.filter(and_(User.email == request.args.get('email'), User.account_type == UserAccountType.APP)).one_or_none()

    except MultipleResultsFound as e:
        raise InternalServerError(description = e.description)

    if user is None or bcrypt.check_password_hash(user.password_hash, request.args.get('password')):
        raise BadRequest(description = 'Invalid email or password.')

    login_user(user)

    return Response(status = HTTPStatus.NO_CONTENT)

@auth_blueprint.route('/login/google', methods = ['GET'])
def requestGoogleLogin():
    if current_user.is_authenticated:
        raise Unauthorized(description = 'You need to log out first.')

    callback = url_for(
        'auth_blueprint.googleCallback',
        next = request.args.get('next') or request.referrer or None,
        _external = True
    )
    return google.authorize(callback = callback)

@auth_blueprint.route('/login/facebook', methods = ['GET'])
def requestFacebookLogin():
    if current_user.is_authenticated:
        raise Unauthorized(description = 'You need to log out first.')
    
    callback = url_for(
        'auth_blueprint.facebookCallback',
        next = request.args.get('next') or request.referrer or None,
        _external = True
    )
    return facebook.authorize(callback = callback)

@auth_blueprint.route('/login/google/callback', methods = ['GET'])
def googleCallback():
    resp = google.authorized_response()

    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    
    session['google_token'] = (resp['access_token'], '')
    me = google.get('userinfo')
    session.pop('google_token')

    try:
        user = User.query.filter(and_(User.email == me.data['email'], User.account_type == UserAccountType.GOOGLE)).one_or_none()

    except MultipleResultsFound as e:
        raise InternalServerError(description = e.description)

    if user is None:
        user = User(
            first_name = me.data['given_name'],
            last_name = me.data['family_name'],
            email = me.data['email'],
            email_confirmed = None,
            password_hash = None,
            account_type = UserAccountType.GOOGLE,
            role = UserRole.USER
        )
        db.session.add(user)
        db.session.commit()
    
    login_user(user)

    return jsonify({'data': me.data, 'redirect': request.args.get('next')})

@auth_blueprint.route('/login/facebook/callback', methods = ['GET'])
def facebookCallback():
    resp = facebook.authorized_response()

    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    if isinstance(resp, OAuthException):
        return 'Access denied: %s' % resp.message

    session['facebook_token'] = (resp['access_token'], '')
    me = facebook.get('/me?fields=first_name,last_name,email,picture.type(large)')
    session.pop('facebook_token')

    try:
        user = User.query.filter(and_(User.email == me.data['email'], User.account_type == UserAccountType.FACEBOOK)).one_or_none()
        
    except MultipleResultsFound as e:
        raise InternalServerError(description = e.description)
    
    if user is None:
        user = User(
            first_name = me.data['first_name'],
            last_name = me.data['last_name'],
            email = me.data['email'],
            email_confirmed = None,
            password_hash = None,
            account_type = UserAccountType.FACEBOOK,
            role = UserRole.USER
        )
        db.session.add(user)
        db.session.commit()

    login_user(user)

    return jsonify({'data': me.data, 'redirect': request.args.get('next')})

@auth_blueprint.route("/logout", methods = ['POST'])
@csrf_token_required
@login_required
def logout():
    session.pop('csrf_token_secret_key')
    logout_user()
    return Response(status = HTTPStatus.NO_CONTENT)