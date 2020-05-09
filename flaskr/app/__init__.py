import logging

from flask import Flask

from .middleware import init_db, init_worker, init_pg
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def register_blueprints(app):
    from .home.views import home
    app.register_blueprint(home)


def create_app(config):
    app = Flask(__name__, template_folder='./templates')

    # Configurations
    app.config.from_object(config)
    logging.basicConfig(level=app.config['LOGGING_LEVEL'])
    # postgres
    db.init_app(app)
    # redis
    app.before_request(init_db)
    # app.before_request(init_worker)
    app.before_first_request(init_pg)

    # Blueprints
    register_blueprints(app)

    # with app.app_context():
    #     try:
    #         db.create_all()
    #     except:
    #         print('Table already exists!')

    # app.before_request(init_pg)

    return app
