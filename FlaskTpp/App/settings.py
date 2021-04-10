import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app_private_key_string = open(os.path.join(BASE_DIR, "alipay_config/app_rsa_private_key.pem")).read()
alipay_public_key_string = open(os.path.join(BASE_DIR, "alipay_config/alipay_rsa_public_key.pem")).read()


class Config:
    DEBUG = False
    TESTING = False
    JSON_AS_ASCII = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 60 * 60


def get_uri(dbinfo):
    engine = dbinfo.get('ENGINE')
    driver = dbinfo.get('DRIVER')
    user = dbinfo.get('USER')
    password = dbinfo.get('PASSWORD')
    host = dbinfo.get('HOST')
    port = dbinfo.get('PORT')
    database = dbinfo.get('DATABASE')

    return "{}+{}://{}:{}@{}:{}/{}".format(engine, driver, user, password, host, port, database)


class DevelopConfig(Config):
    DEBUG = True

    dbinfo = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'pengfan758258',
        'PASSWORD': 'Pf@7758258',
        'HOST': 'rm-bp1nq96t1655pm4djmo.mysql.rds.aliyuncs.com',
        'PORT': '3306',
        'DATABASE': 'FlaskTpp'
    }

    SQLALCHEMY_DATABASE_URI = get_uri(dbinfo)


class TestingConfig(Config):
    TESTING = True

    dbinfo = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'pengfan758258',
        'PASSWORD': 'Pf@7758258',
        'HOST': 'rm-bp1nq96t1655pm4djmo.mysql.rds.aliyuncs.com',
        'PORT': '3306',
        'DATABASE': 'FlaskTpp'
    }

    SQLALCHEMY_DATABASE_URI = get_uri(dbinfo)


class StagingConfig(Config):
    dbinfo = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'pengfan758258',
        'PASSWORD': 'Pf@7758258',
        'HOST': 'rm-bp1nq96t1655pm4djmo.mysql.rds.aliyuncs.com',
        'PORT': '3306',
        'DATABASE': 'FlaskTpp'
    }

    SQLALCHEMY_DATABASE_URI = get_uri(dbinfo)


class ProductConfig(Config):
    dbinfo = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'pengfan758258',
        'PASSWORD': 'Pf@7758258',
        'HOST': 'rm-bp1nq96t1655pm4djmo.mysql.rds.aliyuncs.com',
        'PORT': '3306',
        'DATABASE': 'FlaskTpp'
    }

    SQLALCHEMY_DATABASE_URI = get_uri(dbinfo)


envs = {
    'develop': DevelopConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'product': ProductConfig,
    'default': DevelopConfig
}

# 超级用户列表
ADMIN = ['pf', 'PF']

# 电影背景图片保存路径
FILE_BACKGROUND_PIC_PATH = '/static/uploads/icons'

# 定义电影图片上传路径，是一个绝对路径
UPLOADS_MOVIE_PIC = os.path.join(BASE_DIR, 'static/uploads/icons')
