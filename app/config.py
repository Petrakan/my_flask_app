import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Configuration(object):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://admin:1234@localhost/flask_app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False