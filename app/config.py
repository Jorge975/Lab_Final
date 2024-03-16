import os


class Config:
    # Secret key for the Flask app
    SECRET_KEY = os.environ.get("SECRET_KEY", "your_secret_key")

    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI", "mysql+mysqldb://root:root@localhost/miproyecto")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Add other configuration variables as needed


class DevelopmentConfig(Config):
    DEBUG = True
    #SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/miproyecto/Persons'

class ProductionConfig(Config):
    DEBUG = False
    #SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/miproyecto/Persons'

class TestingConfig(Config):
    TESTING = True
    #SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/miproyecto/Persons'

# Dictionary to map environment names to configuration classes
config_dict = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
    # Add other environments if needed
}
