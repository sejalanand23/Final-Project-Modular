from distutils.log import debug
import os
from flask import Flask, jsonify
from flask_restful import Resource, Api
from application import config 
from application.config import LocalDevelopmentConfig
from application.database import db
from flask_cors import CORS
from application.models import *
from flask_security import Security, SQLAlchemySessionUserDatastore, SQLAlchemyUserDatastore
from application.models import User, Role
from flask_login import LoginManager
from flask_wtf import CSRFProtect
# from wtforms import StringField
from wtforms.validators import DataRequired
from flask_security.forms import RegisterForm,LoginForm,StringField

class ExtendedRegisterForm(RegisterForm):
    username = StringField('username', [DataRequired()])


app = None
api = None

def create_app():
    app = Flask(__name__, template_folder="templates")
    CORS(app)
    # CORS(app,resources={r"/api": {"origins": "*"}})
    # app.config['CORS_HEADERS'] = 'Content-Type'
    if os.getenv('ENV','development') == 'production':
        raise Exception("Currently no production config is setup.")
    else:
        print("Starting local development environment")
        app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    app.app_context().push()
    api = Api(app)
    # CSRFProtect(app)
    db.create_all()
    app.app_context().push()
    # Setup Flask-Security
    user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
    security = Security(app, user_datastore, register_form=ExtendedRegisterForm)
    return app,api

app,api = create_app()

from application.controllers import *

from application.api import *
api.add_resource(UserResource, "/api/user", "/api/user/<email>")
api.add_resource(DeckResource, "/api/deck","/api/deck/<email>")
api.add_resource(CardResource, "/api/card/<card_id>", "/api/card")
api.add_resource(QuizResource,"/api/quiz/<email>/<deck_name>")
api.add_resource(UserDeckResource,"/api/<email>/decks_info")

if __name__ == '__main__':   
    app.run(debug = True)