from flask import Flask

from App.apis import init_apis
from App.ext import init_ext
from App.settings import envs
from App.views import init_views


def create_app(env):
    # 初始化app
    app = Flask(__name__, static_folder="../static")

    # 初始化app配置
    app.config.from_object(envs.get(env))

    # 初始化扩展库
    init_ext(app)

    # 初始化路由
    # init_views(app) # 一般前后端都由自己写的话使用这种方式
    init_apis(app)  # 只开发后端接口

    return app
