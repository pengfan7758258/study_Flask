from flask import Flask

from App.ext import init_ext
from App.settings import envs
from App.views import init_views


def create_app(env):
    app = Flask(__name__)  # 初始化app

    # 加载配置文件
    app.config.from_object(envs.get(env))

    # 加载第三方插件
    init_ext(app)

    # 加载视图函数
    init_views(app)

    return app
