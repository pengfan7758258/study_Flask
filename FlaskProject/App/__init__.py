from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

from App.ext import init_ext
from App.settings import envs
from App.views import blue, second, init_views


def create_app(env):
    # 创建app
    app = Flask(__name__)

    # uri   数据库+驱动：//用户名：密码@主机：端口/具体哪一个库
    # app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///sqlite.db"  # 连接sqlite库
    # app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123@localhost:3306/my_flask"  # 连接mysql数据库
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    app.config.from_object(envs.get(env))
    
    # 扩展库初始化
    init_ext(app)

    # 初始化views --> 注册所有蓝图
    init_views(app)

    return app
