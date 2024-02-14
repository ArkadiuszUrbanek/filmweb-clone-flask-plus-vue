from flask import Blueprint, url_for, request, Response, session, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from flask_mail import Message
from sqlalchemy import and_
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from flask_oauthlib.client import OAuthException
from . import bcrypt, facebook, google, mail, url_safe_token_generator
from ..decorators import csrf_token_required
from models import db, User, Salt
from enums import UserRole, UserAccountType
from http import HTTPStatus
from werkzeug.exceptions import InternalServerError, Unauthorized, BadRequest, Gone
from itsdangerous import SignatureExpired, BadSignature
from secrets import token_hex
from dotenv import dotenv_values

config = dotenv_values('.env')

auth_blueprint = Blueprint('auth_blueprint', __name__, url_prefix = '/auth')

@auth_blueprint.route('/register', methods = ['POST'])
def register():
    email = request.json['email']

    user_entity = User(
        first_name = request.json['firstName'],
        last_name = request.json['lastName'],
        email = email,
        email_confirmed = False,
        gender = request.json['gender'].upper(),
        birth_date = request.json['birthDate'],
        password_hash = bcrypt.generate_password_hash(request.json['password']),
        account_type = UserAccountType.APP,
        role = UserRole.USER
    )

    salt = token_hex(10)

    user_entity.salts.append(
        Salt(
            value = salt,
            valid = True
        )
    )

    db.session.add(user_entity)
    db.session.commit()
    db.session.flush()

    db.session.refresh(user_entity)
    session['user_id'] = user_entity.id

    email_confirmation_link = f'{config["FRONTEND_URL"]}{config["FRONTEND_EMAIL_CONFIRMATION_VIEW_PATH"]}?token={url_safe_token_generator.dumps(obj = email, salt = salt)}'

    email_message = Message(
        subject = 'Email confirmation link',
        recipients = [email],
        html = f'Please confirm your account by <a href="{email_confirmation_link}">clicking here</a>.',
        sender = config['MAIL_USERNAME']
    )

    mail.send(email_message)

    return Response(status = HTTPStatus.CREATED)

@auth_blueprint.route('/email/confirm', methods = ['PATCH'])
def confirmEmail():
    user_id = session.get('user_id', None)

    if user_id is None:
        raise Unauthorized(description = 'Current user cannot confirm the email.')

    try:
        salt_entity = Salt.query.filter(and_(Salt.user_id == user_id, Salt.valid == True)).one()

    except (NoResultFound, MultipleResultsFound) as exception:
        raise InternalServerError(description = exception.message)

    try:
        email = url_safe_token_generator.loads(s = request.json['token'], max_age = 60 * 60 * 24, salt = salt_entity.value)

    except SignatureExpired as exception:
        salt_entity.valid = False
        db.session.commit()
        raise Gone(description = exception.message)
    
    except BadSignature as exception:
        raise BadRequest(description = 'Email confirmation token is invalid.')

    updated_rows_count = User.query \
        .filter(and_(User.email == email, User.account_type == UserAccountType.APP, User.email_confirmed == False)) \
        .update({'email_confirmed': True})
    salt_entity.valid = False
    db.session.commit()

    session.pop('user_id')

    if updated_rows_count == 0:
        raise Unauthorized(description = 'Email address has been already confirmed.')

    return Response(status = HTTPStatus.NO_CONTENT)

@auth_blueprint.route('/email/confirmation-link', methods = ['POST'])
def resendEmailConfirmationLink():
    user_id = session.get('user_id', None)

    if user_id is None:
        raise Unauthorized(description = 'Current user cannot request an email confirmation link.')

    salt_entities = Salt.query.filter_by(user_id = user_id).all()

    is_salt_duplicated = False
    salt = token_hex(10)
    for salt_entity in salt_entities:
        salt_entity.valid = False

        if salt_entity.value == salt:
            is_salt_duplicated = True
    
    while (is_salt_duplicated):
        is_salt_duplicated = False
        salt = token_hex(10)
        for salt_entity in salt_entities:
            if salt_entity.value == salt:
                is_salt_duplicated = True
    
    db.session.add(Salt(value = salt, valid = True, user_id = user_id))
    db.session.commit()

    email = request.json['email']

    email_message = Message(
        subject = 'Email confirmation link',
        sender = config['MAIL_USERNAME'],
        recipients = [email]
    )

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
        user = User.query.filter(and_(User.email == request.json['email'], User.account_type == UserAccountType.APP)).one_or_none()

    except MultipleResultsFound as exception:
        raise InternalServerError(description = exception.message)

    if user is None or not bcrypt.check_password_hash(user.password_hash, request.json['password']):
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

    except MultipleResultsFound as exception:
        raise InternalServerError(description = exception.message)

    if user is None:
        user = User(
            first_name = me.data['given_name'],
            last_name = me.data['family_name'],
            email = me.data['email'],
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
    me = facebook.get('/me?fields=first_name,last_name,email,gender,picture.type(large)')
    session.pop('facebook_token')

    try:
        user = User.query.filter(and_(User.email == me.data['email'], User.account_type == UserAccountType.FACEBOOK)).one_or_none()
        
    except MultipleResultsFound as exception:
        raise InternalServerError(description = exception.message)
    
    if user is None:
        user = User(
            first_name = me.data['first_name'],
            last_name = me.data['last_name'],
            email = me.data['email'],
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
    logout_user()
    return Response(status = HTTPStatus.NO_CONTENT)