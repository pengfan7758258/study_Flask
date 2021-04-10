from flask import Blueprint

blue = Blueprint("blue", __name__)  # 初始化蓝图


def init_views(app):
    app.register_blueprint(blue)  # 注册蓝图到app当中
