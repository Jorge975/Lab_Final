import os

import os
from flask import Config

class TestingConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get("'mysql+mysqldb://root:root@localhost/miproyecto?unix_socket=/path/to/mysqld.sock'")
    DEBUG = True
    TESTING = False

# https://www.pythonanywhere.com/forums/topic/27169/ 
