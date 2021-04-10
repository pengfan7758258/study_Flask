import uuid

from flask_restful import Resource, reqparse, abort, fields, marshal

from App.apis.api_constant import HTTP_CREATE_OK, USER_ACTION_LOGIN, USER_ACTION_REGISTER, HTTP_OK
from App.apis.movie_user.model_utils import get_movie_user
from App.ext import cache
from App.models.movie_user import MovieUser

# 限定输入格式
from App.utils import generate_movie_user_token

parse_base = reqparse.RequestParser()
parse_base.add_argument('password', type=str, required=True, help="请输入密码")
parse_base.add_argument('action', type=str, required=True, help="请确认请求参数")

parse_register = parse_base.copy()
parse_register.add_argument('username', type=str, required=True, help="请输入用户名")
parse_register.add_argument('phone', type=str, required=True, help="请输入手机号")

parse_login = parse_base.copy()
parse_login.add_argument('username', type=str, help="请输入用户名")
parse_login.add_argument('phone', type=str, help="请输入手机号")

# 输出格式，相当于一个模版 开始就定义好，后面不容易出错
movie_user_fields = {
    'username': fields.String,
    'phone': fields.String,
    'password': fields.String(attribute="_password")  # 代表做映射的时候把数据库字段_password给到这个password
}

single_movie_user_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.Nested(movie_user_fields)  # fields.Nested字段嵌套
}


class MovieUsersResource(Resource):

    # @marshal_with(single_movie_user_fields)
    def post(self):
        args = parse_base.parse_args()  # 这个不能放在外面，不然会出现上下文管理的error
        password = args.get('password')
        action = args.get('action').lower()

        if action == USER_ACTION_REGISTER:
            args_register = parse_register.parse_args()
            username = args_register.get('username')
            phone = args_register.get('phone')

            movie_user = MovieUser()
            movie_user.username = username
            movie_user.password = password
            movie_user.phone = phone

            if not movie_user.save():
                abort(400, msg="create fail")

            data = {
                'status': HTTP_CREATE_OK,
                'msg': 'create movie user success',
                'data': movie_user
            }

            return marshal(data, single_movie_user_fields)  # 以模版方式返回数据
        elif action == USER_ACTION_LOGIN:
            args_login = parse_login.parse_args()
            username = args_login.get('username')
            phone = args_login.get('phone')
            user = get_movie_user(username) or get_movie_user(phone)  # 根据用户名和手机号获取用户对象
            if not user:
                abort(400, msg="用户不存在")

            if not user.check_password(password):
                abort(401, msg='密码错误')

            if user.is_delete:  # 被逻辑删除的用户也是不存在的，并且想用这个用户名创建还创建不成功
                abort(401, msg='用户不存在')

            token = generate_movie_user_token()  # 生成token
            cache.set(token, user.id, timeout=60 * 60 * 24 * 7)  # 将token放入cache缓存当中，timeout设置过期时间：单位是s
            # 60 * 60 * 24 * 7代表一周

            data = {
                'msg': 'login success',
                'status': HTTP_OK,
                'token': token,
            }

            return data

        else:  # 当用户动作既不是login也不是register
            abort(400, msg="请提供正确的参数")
