from flask import g
from flask_restful import Resource, reqparse, abort, fields, marshal

from App.apis.api_constant import HTTP_CREATE_OK
from App.apis.cinema_admin.utils import permission_required
from App.models.cinema_admin import CinemaAddress
from App.models.cinema_admin.permission_contants import PERMISSION_WRITE

# 限定输入格式
parse = reqparse.RequestParser()
parse.add_argument("name", required=True, help="请提供电影院的名称")
parse.add_argument("city", required=True, help="请提供所在城市")
parse.add_argument("district", required=True, help="请提供所在区")
parse.add_argument("address", required=True, help="请提供详细地址")
parse.add_argument("phone", required=True, help="请提供联系方式")

"""
    c_user_id = db.Column(db.Integer, db.ForeignKey(CinemaUser.id))  # 添加电影地址的时候必须在电影用户中存在才能添加（因为外键的关系）
    name = db.Column(db.String(64))  # "深圳戏院影城"
    city = db.Column(db.String(16))  # "深圳"
    district = db.Column(db.String(16))  # "罗湖"
    address = db.Column(db.String(128))  # "罗湖区新园路1号东门bu步行街西口"
    phone = db.Column(db.String(32))  # "0755-82175808"
"""

cinema_address_fields = {
    'c_user_id': fields.Integer,
    'name': fields.String,
    'city': fields.String,
    'district': fields.String,
    'address': fields.String,
    'phone': fields.String,
    "score": fields.Float,
    "hallnum": fields.Integer,
    "servicecharge": fields.Float,
    "astrict": fields.Integer
}


class CinemaAddressesResource(Resource):
    def get(self):
        return {'msg': "get ok"}

    @permission_required(PERMISSION_WRITE)  # 验证是否有写的权限
    def post(self):
        args = parse.parse_args()

        name = args.get('name')
        city = args.get('city')
        district = args.get('district')
        address = args.get('address')
        phone = args.get('phone')

        cinema_address = CinemaAddress()
        cinema_address.c_user_id = g.user.id
        cinema_address.name = name
        cinema_address.city = city
        cinema_address.district = district
        cinema_address.address = address
        cinema_address.phone = phone

        if not cinema_address.save():
            abort(400, msg="cinema can't save")

        data = {
            'status': HTTP_CREATE_OK,
            'msg': 'create cinema success',
            'data': marshal(cinema_address, cinema_address_fields)
        }

        return data


class CinemaAddressResource(Resource):
    def get(self, cinema_id):
        pass

    def put(self, cinema_id):
        pass

    def patch(self, cinema_id):
        pass

    def delete(self, cinema_id):
        pass
