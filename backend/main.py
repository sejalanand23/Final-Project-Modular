from distutils.log import debug
import os
from flask import Flask, jsonify
from flask_restful import Resource, Api
from application import config 
from application.config import LocalDevelopmentConfig
from application.database import db
from flask_cors import CORS
# from application.security import *

app = None
api = None

def create_app():
    app = Flask(__name__, template_folder="templates")
    CORS(app)
    if os.getenv('ENV','development') == 'production':
        raise Exception("Currently no production config is setup.")
    else:
        print("Starting local development environment")
        app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    app.app_context().push()
    api = Api(app)
    db.create_all()
    app.app_context().push()
    # sec.init_app(app, user_datastore)
    # return app
    return app,api

app,api = create_app()

from application.controllers import *

from application.api import *
api.add_resource(UserResource, "/api/user", "/api/user/<username>")
api.add_resource(DeckResource, "/api/deck","/api/deck/<deck_name>","/api/deck/<username>","/api/deck/<username>/<deck_name>")
api.add_resource(CardResource, "/api/card")

if __name__ == '__main__':   
    app.run(debug = True)