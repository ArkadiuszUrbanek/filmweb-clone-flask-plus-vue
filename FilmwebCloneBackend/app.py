from flask import Flask
from Models import db
from Blueprints import oauth, auth_blueprint
from dotenv import dotenv_values

if __name__ == '__main__':
    config = dotenv_values('.env')

    app = Flask(__name__)
    app.config['SECRET_KEY'] = config['APP_SECRET_KEY']
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{config["MYSQL_USERNAME"]}:{config["MYSQL_PASSWORD"]}@localhost/{config["MYSQL_DATABASE_NAME"]}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    oauth.init_app(app)

    with app.app_context(): 
        db.create_all()
    
    app.register_blueprint(auth_blueprint)
    app.run(host = '127.0.0.1', port = 5000, debug = True, ssl_context = 'adhoc')
