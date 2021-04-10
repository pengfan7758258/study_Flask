from flask import g
from flask_restful import Resource, reqparse, abort, fields, marshal

from App.apis.api_constant import HTTP_CREATE_OK
from App.apis.cinema_admin.utils import login_required
from App.models.cinema_admin import CinemaAddress
from App.models.cinema_admin.cinema_hall_model import Hall

parse = reqparse.RequestParser()
parse.add_argument('h_num', required=True, help="请提供放映厅编号")
parse.add_argument('h_seats', required=True, help="请提供放映厅布局")
parse.add_argument('address_id', type=int, required=True, help="请提供影院地址")

hall_fields = {
    'address_id': fields.Integer(attribute='h_address_id'),
    'h_num': fields.Integer,
    'h_seats': fields.String
}


class CinemaHallsResource(Resource):
    def get(self):
        pass

    @login_required
    def post(self):
        args = parse.parse_args()

        h_num = args.get('h_num')
        h_seats = args.get('h_seats')
        address_id = args.get('address_id')

        cinema_addresses = CinemaAddress.query.filter_by(c_user_id=g.user.id).all()
        if cinema_addresses:
            cinema_addresses_id = [cinema_address.id for cinema_address in cinema_addresses]
            print(cinema_addresses_id)
            if address_id not in cinema_addresses_id:
                abort(400, msg="error action")
        else:
            abort(400, msg="error action")

        hall = Hall()
        hall.h_address_id = address_id
        hall.h_num = h_num
        hall.h_seats = h_seats

        if not hall.save():
            abort(400, msg="create hall fail")

        data = {
            'msg': 'create hall success',
            'status': HTTP_CREATE_OK,
            'data': marshal(hall, hall_fields)
        }

        return data
