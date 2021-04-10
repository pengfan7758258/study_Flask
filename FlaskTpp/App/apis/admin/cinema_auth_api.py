from flask_restful import Resource, fields, marshal, reqparse, abort

from App.apis.admin.utils import login_required
from App.apis.api_constant import HTTP_OK
from App.models.cinema_admin import CinemaUser

cinema_user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'phone': fields.String,
    'password': fields.String(attribute="_password"),  # 代表做映射的时候把数据库字段_password给到这个password
    "is_verify": fields.Boolean
}

single_cinema_user_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.Nested(cinema_user_fields)  # fields.Nested字段嵌套
}

multi_cinema_user_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(cinema_user_fields))  # fields.Nested字段嵌套
}


class AdminCinemaUsersResource(Resource):

    @login_required
    def get(self):
        cinema_users = CinemaUser.query.all()

        data = {
            'status': HTTP_OK,
            'msg': 'ok',
            'data': cinema_users

        }

        return marshal(data, multi_cinema_user_fields)


parse = reqparse.RequestParser()
parse.add_argument('is_verify', required=True, type=bool, help="请提供操作")


class AdminCinemaUserResource(Resource):
    @login_required
    def get(self, cinema_id):
        cinema_user = CinemaUser.query.get(cinema_id)

        data = {
            'status': HTTP_OK,
            'msg': 'ok',
            'data': cinema_user
        }

        return marshal(data, single_cinema_user_fields)

    @login_required
    def patch(self, cinema_id):
        args = parse.parse_args()
        is_verify = args.get('is_verify')
        cinema_user = CinemaUser.query.get(cinema_id)

        cinema_user.is_verify = is_verify

        if not cinema_user.save():
            abort(400, msg="change fail")

        data = {
            'status': HTTP_OK,
            'msg': 'ok',
            'data': cinema_user
        }

        return marshal(data, single_cinema_user_fields)
