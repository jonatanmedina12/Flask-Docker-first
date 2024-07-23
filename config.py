import os


class Config:
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'Dev'
    SWAGGER = {
        'title': 'Flask API',
        'uiversion': 3
    }