from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS
from models import db
from blueprints import oauth, auth_blueprint, bcrypt, login_manager
from dotenv import dotenv_values

if __name__ == '__main__':
    config = dotenv_values('.env')

    app = Flask(__name__)

    app.config['SECRET_KEY'] = config['APP_SECRET_KEY']
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['SESSION_COOKIE_SECURE'] = True
    app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{config["MYSQL_USERNAME"]}:{config["MYSQL_PASSWORD"]}@localhost/{config["MYSQL_DATABASE_NAME"]}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    oauth.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    CORS(app, resources = {
        r"/*": {
            'origins': ['http://localhost:5137'],
            'methods': ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'],
            'expose_headers': None,
            'allow_headers': ['*'],
            'supports_credentials': True,
            }
        })

    with app.app_context():
        db.create_all()

    app.register_blueprint(auth_blueprint)
    app.run(host = '127.0.0.1', port = 5000, debug = True, ssl_context = 'adhoc')
