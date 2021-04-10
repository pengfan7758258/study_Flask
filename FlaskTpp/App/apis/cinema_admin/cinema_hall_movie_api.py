from flask import g
from flask_restful import Resource, reqparse, abort, fields, marshal

from App.apis.api_constant import HTTP_CREATE_OK
from App.apis.cinema_admin.utils import login_required
from App.models.cinema_admin import CinemaAddress
from App.models.cinema_admin.cinema_hall_model import Hall
from App.models.cinema_admin.cinema_hall_movie_model import HallMovie
from App.models.cinema_admin.cinema_movie_model import CinemaMovies

parse = reqparse.RequestParser()
parse.add_argument('movie_id', required=True, help="请提供电影")
parse.add_argument('hall_id', required=True, help="请提供放映厅")
parse.add_argument('h_time', required=True, help="请提供电影放映时间")

hall_movie_fields = {
    'movie_id': fields.Integer(attribute='h_movie_id'),
    'hall_id': fields.Integer(attribute='h_hall_id'),
    'h_time': fields.DateTime
}


class CinemaHallMoviesResource(Resource):

    @login_required
    def get(self):
        return {'msg': 'get ok'}

    @login_required
    def post(self):
        args = parse.parse_args()

        movie_id = args.get('movie_id')
        hall_id = args.get('hall_id')
        h_time = args.get('h_time')

        # 验证 movie_id 是否已经购买
        cinema_movies = CinemaMovies.query.filter_by(c_user_id=g.user.id).all()

        movie_ids = [cinema_movie.movie_id for cinema_movie in cinema_movies]

        if movie_id not in movie_ids:
            abort(403, msg="该电影还未购买")

        # hall_id 是否是当前用户
        cinema_addresses = CinemaAddress.query.filter_by(c_user_id=g.user.id).all()
        hall_ids = []

        for cinema_address in cinema_addresses:
            for hall in Hall.query.filter(h_address_id=cinema_address.id).all():
                hall_ids.append(hall.id)

        if hall_id not in hall_ids:
            abort(403, msg="该大厅未找到")

        # h_time 进行时间限制(不低于当前时间或不低于当前时间半小时，不能超前购买3天)
        # 同时间的同影厅是否有不同的电影排挡

        hall_movie = HallMovie()
        hall_movie.h_hall_id = hall_id
        hall_movie.h_time = h_time
        hall_movie.h_movie_id = movie_id

        if not hall_movie.save():
            abort(400, msg="排挡失败，请稍后尝试")

        data = {
            'status': HTTP_CREATE_OK,
            'msg': 'ok',
            'data': marshal(hall_movie, hall_movie_fields)
        }

        return data
