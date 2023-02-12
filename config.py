from os import environ
from dotenv import load_dotenv, find_dotenv
import os
import logging

load_dotenv(find_dotenv(raise_error_if_not_found=True))

# database uri: database.db file in project's directory
_basedir = os.path.abspath(os.path.dirname(__file__))
db_file_path = os.path.join(_basedir, 'database.db')
db_uri = 'sqlite:///' + db_file_path


class AppConfig(object):
    """Set Flask config variables."""

    # FLASK_ENV = 'development'
    SECRET_KEY = environ.get('SECRET_KEY')
    # STATIC_FOLDER = 'static'
    # TEMPLATES_FOLDER = 'templates'
    # TEMPLATES_AUTO_RELOAD = True

    # Database
    SQLALCHEMY_DATABASE_URI = db_uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Logging
    LOG_FILE = _basedir + '/logs/flaskapp.log'
    LOG_LEVEL = logging.ERROR  # CRITICAL,ERROR,WARNING,INFO,DEBUG,NOTSET

    @staticmethod
    def init_app(app):
        pass


class DevelopmentAppConfig(AppConfig):
    DEBUG = True
    LOG_LEVEL = logging.DEBUG
    # SQLALCHEMY_RECORD_QUERIES = True


class TestingAppConfig(AppConfig):
    TESTING = True
    LOG_LEVEL = logging.INFO
    # SQLALCHEMY_ECHO = True
    WTF_CSRF_ENABLED = False


class ProductionAppConfig(AppConfig):
    DEBUG = False
    TESTING = False
    LOG_LEVEL = logging.WARNING

    @classmethod
    def init_app(cls, app):
        # multi-step setups could go here
        AppConfig.init_app(app)


config = {
    'development': DevelopmentAppConfig,
    'testing': TestingAppConfig,
    'production': ProductionAppConfig,
    'default': DevelopmentAppConfig
}
