from .first_blue import blue
from .second_blue import second


# 初始化views-->注册所有蓝图
def init_views(app):
    app.register_blueprint(blueprint=blue)
    app.register_blueprint(blueprint=second)

