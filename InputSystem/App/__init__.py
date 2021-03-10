from flask import Flask

from App.apis import init_api
from App.ext import init_ext
from App.middleware import load_middleware
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
    init_api(app)

    # 加载中间件
    load_middleware(app)

    return app
