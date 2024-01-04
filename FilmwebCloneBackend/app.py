from flask import Flask, Response, current_app, request
from flask_login import current_user
from flask_cors import CORS
from flask_wtf.csrf import generate_csrf
from models import db
from blueprints import oauth, auth_blueprint, bcrypt, login_manager, csrf, protected_funcs, error_blueprint
from dotenv import dotenv_values
from secrets import token_hex

config = dotenv_values('.env')

app = Flask(__name__)

app.config['SECRET_KEY'] = config['APP_SECRET_KEY']
app.config['SESSION_COOKIE_DOMAIN'] = '127.0.0.1'
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = None
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{config["MYSQL_USERNAME"]}:{config["MYSQL_PASSWORD"]}@localhost/{config["MYSQL_DATABASE_NAME"]}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['WTF_CSRF_ENABLED'] = True
app.config['WTF_CSRF_CHECK_DEFAULT'] = False
app.config['WTF_CSRF_SECRET_KEY'] = token_hex()
app.config['WTF_CSRF_SSL_STRICT'] = False
app.config['WTF_CSRF_METHODS'] = {'GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'}

db.init_app(app)
oauth.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)
csrf.init_app(app)

CORS(app, resources = {
    r"/*": {
        'origins': ['http://localhost:5137'],
        'methods': ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'],
        'supports_credentials': True,
    }
})

with app.app_context():
    db.create_all()

@app.before_request
def check_csrf():
    if current_user.is_authenticated or current_user.csrf_token_secret_key != None:
        current_app.config.update(WTF_CSRF_SECRET_KEY = current_user.csrf_token_secret_key)
    
    if request.endpoint != None:
        view = current_app.view_functions.get(request.endpoint)
        dest = f'{view.__module__}.{view.__name__}'
    
        if dest in protected_funcs:
            csrf.protect()

@app.after_request
def set_csrf_cookie(response: Response):
    current_user.csrf_token_secret_key = token_hex()
    current_app.config.update(WTF_CSRF_SECRET_KEY = current_user.csrf_token_secret_key)
    response.set_cookie(key = 'X-CSRFToken', 
                        value = generate_csrf(),
                        domain = '127.0.0.1',
                        secure = True,
                        httponly = False,
                        samesite = None)
    return response

app.register_blueprint(auth_blueprint)
app.register_blueprint(error_blueprint)

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 5000, debug = True, ssl_context = 'adhoc')
