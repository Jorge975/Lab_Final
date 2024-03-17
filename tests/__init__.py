import os

import os
from flask import Config

class TestingConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get("postgresql://user:password@localhost:5432/miproyecto")
    DEBUG = True
    TESTING = False

# https://www.pythonanywhere.com/forums/topic/27169/ 
