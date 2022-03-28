from distutils.log import debug
import os
from flask import Flask
from flask_restful import Api
# from gevent import config 
from application.config import LocalDevelopmentConfig
from application.database import db
from flask_cors import CORS
from application.models import *
from flask_security import SQLAlchemySessionUserDatastore,Security
from application import workers
# from flask_sse import sse

app = None
api = None
celery = None


def create_app():
    app = Flask(__name__, template_folder="templates")

    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    if os.getenv('ENV','development') == 'production':
        raise Exception("Currently no production config is setup.")
    else:
        print("Starting local development environment")
        app.config.from_object(LocalDevelopmentConfig)

    db.init_app(app)
    
    app.app_context().push()


    ma.init_app(app)
    app.app_context().push()
    db.create_all()

    api = Api(app)
      
    app.app_context().push()

    # Setup Flask-Security
    user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
    security = Security(app,user_datastore)

    # cache = Cache(app)
    # app.app_context().push()

    celery = workers.celery
    celery.conf.update(
        broker_url = app.config['CELERY_BROKER_URL'],
        result_backend = app.config['CELERY_RESULT_BACKEND']
    )
    celery.Task = workers.ContextTask
    app.app_context().push()

    return app,api,celery

app,api,celery = create_app()

# app.register_blueprint(sse, url_prefix = '/stream')

from application.controllers import *

from application.api import *

api.add_resource(DeckResource, "/api/deck","/api/deck/<email>","/api/deck/edit/<deck_name>")
api.add_resource(CardResource, "/api/card/<card_id>", "/api/card")
api.add_resource(QuizResource,"/api/quiz/<email>/<deck_name>")
api.add_resource(ScoreResource,"/api/deck/scoring")
api.add_resource(Decks_Export_Task,"/api/export/decks/<email>")
api.add_resource(Cards_Export_Task,"/api/export/cards/<deck_name>/<email>")

if __name__ == '__main__':   
    app.run(debug = True)