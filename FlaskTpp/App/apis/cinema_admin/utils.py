from functools import wraps

from flask import request, g
from flask_restful import abort

from App.apis.cinema_admin.model_utils import get_cinema_user
from App.ext import cache

# g对象在 一次请求 中的所有的代码的地方，都是可以使用的

# 验证token
from App.utils import CINEMA_USER


def _verity():
    token = request.args.get('token')
    if not token:  # 没有token说明没有登陆
        abort(401, msg="Not login")

    if not token.startswith(CINEMA_USER):
        abort(401, msg="no access")

    user_id = cache.get(token)
    if not user_id:
        abort(401, msg="auth is available")

    user = get_cinema_user(user_id)
    if not user:
        abort(401, msg="auth is available")

    g.user = user
    g.auth = token


# 登陆验证  装饰器
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        _verity()

        return func(*args, **kwargs)

    return wrapper


# 权限验证 装饰器
def permission_required(permission):
    def permission_required_wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            _verity()

            if not g.user.check_permission(permission):
                abort(403, msg="user can't access")

            return func(*args, **kwargs)

        return wrapper

    return permission_required_wrapper
