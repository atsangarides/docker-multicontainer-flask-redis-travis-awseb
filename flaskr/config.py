import logging
import os


class Config(object):
    TESTING = False
    LOGGING_LEVEL = logging.INFO
    SECRET_KEY = 'mysecret'
    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{os.environ.get('PGUSER')}:{os.environ.get('PGPASSWORD')}" \
                              f"@{os.environ.get('PGHOST')}:{os.environ.get('PGPORT')}/{os.environ.get('PGDATABASE')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


class DevelopmentConfig(Config):
    DEBUG = True
    LOGGING_LEVEL = logging.DEBUG


config = {
    'prod': 'config.ProductionConfig',
    'dev': 'config.DevelopmentConfig',
    'test': 'config.TestConfig'
}
