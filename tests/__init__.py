import os
from flask import Config

class DevelopementConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get("mysql://")
    DEBUG = True
    TESTING = False

# https://www.pythonanywhere.com/forums/topic/27169/ 
