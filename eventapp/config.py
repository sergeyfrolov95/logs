import os

# Base configuration class
class Base(object):

    # Debug
    DEBUG = False
    TESTING = False

    # Localization
    ENCODING = 'utf-8'
    BABEL_DEFAULT_LOCALE = 'ru'
    SECRET_KEY = 'such_secret'

    # Database
    SQLALCHEMY_DATABASE_URI = 'postgresql://sergey@localhost/events'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DOMAIN = 'localhost'

# Production configuration class
class Production(Base):

    # Debug
    DEBUG = False
    TESTING = False


# Development configuration class
class Development(Base):

    # Debug
    DEBUG = True
    TESTING = True
