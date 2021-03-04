from werkzeug.exceptions import HTTPException

from .exception import ApiException
from .newsView import news_blue
from ..models import db


def global_error_handler(app):
    # 为了捕捉所有的异常, 我们需要绑定异常的基类 Exception, Flask>1.0
    @app.errorhandler(Exception)
    def framework_error(e):
        # ApiExcetion
        # HttpException
        # Exception
        if isinstance(e, HTTPException):
            code = e.code
            msg = e.description
            return ApiException(code=code, msg=msg)
        else:
            if not app.config['DEBUG']:
                return ApiException()
            raise e


def init_views(app):
    app.register_blueprint(news_blue)

    global_error_handler(app)
