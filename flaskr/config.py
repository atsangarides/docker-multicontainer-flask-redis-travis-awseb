import logging
import os


class Config(object):
    DEBUG = False
    TESTING = False
    LOGGING_LEVEL = logging.INFO
    SECRET_KEY = 'mysecret'
    REDIS_HOST = os.environ.get('REDIS_HOST')
    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{os.environ.get('PGUSER')}:{os.environ.get('PGPASSWORD')}" \
                              f"@{os.environ.get('PGHOST')}:{os.environ.get('PGPORT')}/{os.environ.get('PGDATABASE')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


class DevelopmentConfig(Config):
    DEBUG = True
    LOGGING_LEVEL = logging.DEBUG
