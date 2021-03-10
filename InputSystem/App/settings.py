import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = os.environ.get('FLASK_ENV', 'default')


# 开发环境配置
def get_uri(dbinfo):
    engine = dbinfo.get('ENGINE')
    driver = dbinfo.get('DRIVER', "")
    user = dbinfo.get('USER', '')
    password = dbinfo.get('PASSWORD', '')
    host = dbinfo.get('HOST', '')["EXTRANET"] if env != "product" else dbinfo.get('HOST', '')["INTRANET"]
    port = dbinfo.get('PORT', '')
    database = dbinfo.get('DATABASE')
    return "{}+{}://{}:{}@{}:{}/{}".format(engine, driver, user, password, host, port, database)


class Config:
    DEBUG = False

    TESTING = False

    SECRET_KEY = 'PF'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CACHE_TYPE = 'filesystem'  # 使用文件系统来存储缓存的值
    CACHE_DIR = os.path.join(BASE_DIR, 'App/cache_dir')

    MAIL_SERVER = 'smtp.163.com'

    MAIL_PORT = 25

    MAIL_USERNAME = 'pengfan929848421@163.com'

    # MAIL_PASSWORD = 'PF929848421'
    MAIL_PASSWORD = 'XWNEUHSIDVGCBPSY'

    MAIL_DEFAULT_SENDER = MAIL_USERNAME


class DevelopConfig(Config):
    DEBUG = True

    dbinfo = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'ai_rds_dev',
        'PASSWORD': 'FMAI2020#^%#dev',
        # 'HOST': {"EXTRANET": 'rm-8vbv370z0d62qy23sao.mysql.zhangbei.rds.aliyuncs.com',
        #          "INTRANET": 'rm-8vbv370z0d62qy23s.mysql.zhangbei.rds.aliyuncs.com'},
        'HOST': {"EXTRANET": 'rm-8vb306n86rr1g506bco.mysql.zhangbei.rds.aliyuncs.com',
                 "INTRANET": 'rm-8vb306n86rr1g506b.mysql.zhangbei.rds.aliyuncs.com'},
        'PORT': '3306',
        'DATABASE': 'dev_hj_genealogy'
    }

    SQLALCHEMY_DATABASE_URI = get_uri(dbinfo)


# 测试环境
class TestingConfig(Config):
    TESTING = True

    dbinfo = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'ai_rds_dev',
        'PASSWORD': 'FMAI2020#^%#dev',
        # 'HOST': {"EXTRANET": 'rm-8vbv370z0d62qy23sao.mysql.zhangbei.rds.aliyuncs.com',
        #          "INTRANET": 'rm-8vbv370z0d62qy23s.mysql.zhangbei.rds.aliyuncs.com'},
        'HOST': {"EXTRANET": 'rm-8vb306n86rr1g506bco.mysql.zhangbei.rds.aliyuncs.com',
                 "INTRANET": 'rm-8vb306n86rr1g506b.mysql.zhangbei.rds.aliyuncs.com'},
        'PORT': '3306',
        'DATABASE': 'dev_hj_genealogy'
    }

    SQLALCHEMY_DATABASE_URI = get_uri(dbinfo)


# 演示环境
class StagingConfig(Config):
    dbinfo = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'ai_rds_dev',
        'PASSWORD': 'FMAI2020#^%#dev',
        # 'HOST': {"EXTRANET": 'rm-8vbv370z0d62qy23sao.mysql.zhangbei.rds.aliyuncs.com',
        #          "INTRANET": 'rm-8vbv370z0d62qy23s.mysql.zhangbei.rds.aliyuncs.com'},
        'HOST': {"EXTRANET": 'rm-8vb306n86rr1g506bco.mysql.zhangbei.rds.aliyuncs.com',
                 "INTRANET": 'rm-8vb306n86rr1g506b.mysql.zhangbei.rds.aliyuncs.com'},
        'PORT': '3306',
        'DATABASE': 'dev_hj_genealogy'
    }

    SQLALCHEMY_DATABASE_URI = get_uri(dbinfo)


# 生产环境
class ProductConfig(Config):
    dbinfo = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'ai_rds_dev',
        'PASSWORD': 'FMAI2020#^%#dev',
        # 'HOST': {"EXTRANET": 'rm-8vbv370z0d62qy23sao.mysql.zhangbei.rds.aliyuncs.com',
        #          "INTRANET": 'rm-8vbv370z0d62qy23s.mysql.zhangbei.rds.aliyuncs.com'},
        'HOST': {"EXTRANET": 'rm-8vb306n86rr1g506bco.mysql.zhangbei.rds.aliyuncs.com',
                 "INTRANET": 'rm-8vb306n86rr1g506b.mysql.zhangbei.rds.aliyuncs.com'},
        'PORT': '3306',
        'DATABASE': 'dev_hj_genealogy'
    }

    SQLALCHEMY_DATABASE_URI = get_uri(dbinfo)


envs = {
    'develop': DevelopConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'product': ProductConfig,
    'default': DevelopConfig
}
