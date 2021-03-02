import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_url(dbinfo):
    engine = dbinfo.get('ENGINE', None)
    driver = dbinfo.get('DRIVER', None)
    user = dbinfo.get('USER', None)
    password = dbinfo.get('PASSWORD', None)
    host = dbinfo.get('HOST', None)
    port = dbinfo.get('PORT', None)
    database = dbinfo.get('DATABASE', None)

    return "{}+{}://{}:{}@{}:{}/{}".format(engine, driver, user, password, host, port, database)


class Config:
    DEBUG = False

    TESTING = False

    SECRET_KEY = 'PF'

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    DEBUG = True

    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        'PASSWORD': "123",
        "HOST": "localhost",
        "PORT": "3306",
        "DATABASE": "my_flask"
    }

    SQLALCHEMY_DATABASE_URI = get_url(dbinfo)


class TestingConfig(Config):
    TESTING = True

    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        'PASSWORD': "123",
        "HOST": "localhost",
        "PORT": "3306",
        "DATABASE": "my_flask"
    }

    SQLALCHEMY_DATABASE_URI = get_url(dbinfo)


class StagingConfig(Config):
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        'PASSWORD': "123",
        "HOST": "localhost",
        "PORT": "3306",
        "DATABASE": "my_flask"
    }

    SQLALCHEMY_DATABASE_URL = get_url(dbinfo)


class ProductConfig(Config):
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        'PASSWORD': "123",
        "HOST": "localhost",
        "PORT": "3306",
        "DATABASE": "my_flask"
    }

    SQLALCHEMY_DATABASE_URI = get_url(dbinfo)


envs = {
    'develop': DevelopConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'product': ProductConfig,
    'default': DevelopConfig
}
