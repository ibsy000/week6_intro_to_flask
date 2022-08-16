import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # settling up the configuration for the application. Pull from enviroment variables using os.environ.get()
    SECRET_KEY = os.environ.get('SECRET KEY') or 'you_will_never_know'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False