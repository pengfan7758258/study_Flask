from flask import request


def load_middleware(app):
    @app.before_request
    def before():
        pass
        """
            统计
            优先级
            反爬
                频率
            用户认证
            用户权限s
        """

    @app.after_request
    def after(resp):

        return resp
