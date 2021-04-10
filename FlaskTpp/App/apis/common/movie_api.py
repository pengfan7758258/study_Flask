import os

from flask_restful import Resource, reqparse, abort, marshal, fields, marshal_with

from App.apis.admin.utils import login_required
from App.apis.api_constant import HTTP_CREATE_OK, HTTP_OK
from App.apis.common.utils import filename_transfer
from App.models.common.movie_model import Movie
import werkzeug.datastructures

"""
    showname = db.Column(db.String(64))  # "梭哈人生"
    shownameen = db.Column(db.String(128))  # "The Drifting Red Balloon"
    director = db.Column(db.String(64))  # "郑来态"
    leadingRole = db.Column(db.String(256))  # "谭佑铭，施子霏，赵韩缨子，孟智超"
    type = db.Column(db.String(64))  # "剧情，爱情，喜剧"
    country = db.Column(db.String(64))  # "中国大陆"
    language = db.Column(db.String(64))  # "汉语普通话"
    duration = db.Column(db.Integer, default=90)  # "90"
    screeningmodel = db.Column(db.String(32))  # "4D"
    openday = db.Column(db.DateTime)  # date("2018-01-30 00:00:00")
    backgroundpicture = db.Column(db.String(256))  # i1/JKLJDLKJFOISDJFOI_.jpg
"""
# 定义数据输入的格式
parse = reqparse.RequestParser()
parse.add_argument("showname", type=str, required=True, help="must supply showname")
parse.add_argument("shownameen", type=str, required=True, help="must supply shownameen")
parse.add_argument("director", type=str, required=True, help="must supply director")
parse.add_argument("leadingRole", type=str, required=True, help="must supply leadingRole")
parse.add_argument("type", type=str, required=True, help="must supply type")
parse.add_argument("country", type=str, required=True, help="must supply country")
parse.add_argument("language", type=str, required=True, help="must supply language")
parse.add_argument("duration", type=str, required=True, help="must supply duration")
parse.add_argument("screeningmodel", type=str, required=True, help="must supply screeningmodel")
parse.add_argument("openday", type=str, required=True, help="must supply openday")
parse.add_argument("backgroundpicture", type=werkzeug.datastructures.FileStorage, required=True,
                   help="must supply backgroundpicture", location=['files'])

# 定义数据输出的格式
movie_fields = {
    "showname": fields.String,
    "shownameen": fields.String,
    "director": fields.String,
    "leadingRole": fields.String,
    "type": fields.String,
    "country": fields.String,
    "language": fields.String,
    "duration": fields.Integer,
    "screeningmodel": fields.String,
    "openday": fields.DateTime,
    "backgroundpicture": fields.String,
}

multi_movie_fields = {
    'status': fields.String,
    'msg': fields.String,
    'data': fields.List(fields.Nested(movie_fields))
}


class MoviesResource(Resource):

    @marshal_with(multi_movie_fields)
    def get(self):
        movies = Movie.query.all()

        data = {
            'status': HTTP_OK,
            'msg': 'ok',
            'data': movies
        }

        return data

    @login_required
    def post(self):
        args = parse.parse_args()

        showname = args.get('showname')
        shownameen = args.get('shownameen')
        director = args.get('director')
        leadingRole = args.get('leadingRole')
        movie_type = args.get('type')
        country = args.get('country')
        language = args.get('language')
        duration = args.get('duration')
        screeningmodel = args.get('screeningmodel')
        openday = args.get('openday')
        backgroundpicture = args.get('backgroundpicture')

        movie = Movie()
        movie.showname = showname
        movie.shownameen = shownameen
        movie.director = director
        movie.leadingRole = leadingRole
        movie.type = movie_type
        movie.country = country
        movie.language = language
        movie.duration = duration
        movie.screeningmodel = screeningmodel
        movie.openday = openday
        # 服务器图片上传保存路径-->存储图片用
        save_path, upload_path = filename_transfer(backgroundpicture.filename)
        backgroundpicture.save(save_path)

        movie.backgroundpicture = upload_path  # 相对路径进行数据库存储位置，显示到数据库中

        if not movie.save():
            abort(400, msg="can't create movie")

        data = {
            'status': HTTP_CREATE_OK,
            'msg': 'create success',
            'data': marshal(movie, movie_fields)
        }

        return data


class MovieResource(Resource):
    def get(self, movie_id):
        movie = Movie.query.get(movie_id)

        if not movie:
            abort(404, msg="movie is not exist")

        data = {
            'status': HTTP_OK,
            'msg': 'ok',
            'data': marshal(movie, movie_fields)
        }

        return data

    @login_required
    def patch(self, movie_id):
        return {'msg': 'patch ok'}

    @login_required
    def put(self, movie_id):
        return {'msg': 'put ok'}

    @login_required
    def delete(self, movie_id):
        return {'msg': 'delete ok'}
