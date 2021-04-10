import datetime

from flask import g
from flask_restful import Resource, reqparse, abort, fields, marshal
from sqlalchemy import or_, and_

from App.apis.api_constant import HTTP_CREATE_OK
from App.apis.movie_user.utils import login_required, permission_required
from App.models.cinema_admin.cinema_hall_model import Hall
from App.models.cinema_admin.cinema_hall_movie_model import HallMovie
from App.models.movie_user.movie_order_model import MovieOrder, ORDER_STATUS_PAYED_NOT_GET, ORDER_STATUS_NOT_PAY, \
    ORDER_STATUS_GET
from App.models.movie_user.movie_user_model import VIP_USER

parse = reqparse.RequestParser()
parse.add_argument("hall_movie_id", required=True, help="请提供排挡信息")
parse.add_argument("o_seats", required=True, help="请正确选择座位")

movie_order_fields = {
    'o_price': fields.Float,
    'o_seats': fields.String,
    'o_hall_movie_id': fields.Integer
}


class MovieOrdersResource(Resource):  # 电影订单（多个）
    @login_required  # 有了装饰器验证登陆，那么可以直接编写登陆后的操作
    def post(self):
        args = parse.parse_args()

        hall_movie_id = args.get('hall_movie_id')
        o_seats = args.get('o_seats')

        hall = Hall.query.get(HallMovie.query.get(hall_movie_id).h_hall_id)

        # o_seats存在，没有被买也没有被锁单
        # 剔除下单和锁单的座位
        movie_orders_buy = MovieOrder.query.filter(MovieOrder.o_hall_movie_id == hall_movie_id).filter(
            or_(MovieOrder.o_status == ORDER_STATUS_PAYED_NOT_GET, MovieOrder.o_status == ORDER_STATUS_GET)).all()

        movie_orders_lock = MovieOrder.query.filter(MovieOrder.o_hall_movie_id == hall_movie_id).filter(
            and_(MovieOrder.o_status == ORDER_STATUS_NOT_PAY, MovieOrder.o_time > datetime.datetime.now())).all()

        seats = []

        for movie_order in movie_orders_buy:
            sold_seats = movie_order.o_seats.split("#")
            seats.extend(sold_seats)

        for movie_order in movie_orders_lock:
            sold_seats = movie_order.o_seats.split("#")
            seats.extend(sold_seats)

        all_seats = hall.h_seats.split("#")
        can_buy = list(set(all_seats) - set(seats))

        want_buy = o_seats.split('#')

        for item in want_buy:
            if item not in can_buy:
                abort(400, msg="锁座失败")

        user = g.user

        movie_order = MovieOrder()
        movie_order.o_hall_movie_id = hall_movie_id
        movie_order.o_seats = o_seats
        movie_order.o_user_id = user.id
        movie_order.o_time = datetime.datetime.now() + datetime.timedelta(minutes=15)

        if not movie_order.save():
            abort(400, msg="下单失败")

        data = {
            'status': HTTP_CREATE_OK,
            'msg': 'ok',
            'data': marshal(movie_order, movie_order_fields)
        }

        return data


class MovieOrderResource(Resource):  # 电影订单（单个）
    @permission_required(VIP_USER)  # 有了装饰器验证权限，那么可以直接编写拥有指定权限后的操作
    def put(self, order_id):
        return {'msg': 'put order success'}
