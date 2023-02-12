# import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import config

db = SQLAlchemy()


def create_app(config_name='default'):
    """
    init app, config, blueprints, database
    :return:
    """
    app = Flask(__name__)

    # app.config.from_object(Config)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # init_logging(app)

    db.init_app(app)

    # will be used to run migration later
    migrate = Migrate(app, db)

    # adding blueprints here
    from .students import student_bp
    app.register_blueprint(student_bp)

    from .device import device_bp
    app.register_blueprint(device_bp)

    # create database and tables if not exists
    with app.app_context():
        # db.drop_all()
        db.create_all()

    return app


# def init_logging(app):
#     import logging
#
#     if not os.path.exists(app.config['LOG_FILE']):
#         os.makedirs(os.path.dirname(app.config['LOG_FILE']), exist_ok=True)
#
#     log_format = '%(asctime)s [%(threadName)-10.10s] [%(levelname)-5.5s]  %(message)s'
#
#     logging.basicConfig(filename=app.config['LOG_FILE'], level=app.config['LOG_LEVEL'], format=log_format)
    # logging.debug("init_logging( filename = %s, level = %i )" % (app.config['LOG_FILE'], app.config['LOG_LEVEL']))
