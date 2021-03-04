from flask import Flask

from App.ext import init_ext
from App.settings import envs
from App.views import init_views


def create_app(env):
    # 创建Flask对象
    app = Flask(__name__)

    # 初始化配置
    app.config.from_object(envs.get(env))

    # 初始化扩展插件 除路由之外的
    init_ext(app)

    # 加载路由
    init_views(app)

    return app
