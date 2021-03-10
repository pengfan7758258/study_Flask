from flask_restful import Api

from App.apis.goods_api import GoodsListResource, GoodsResource
from App.apis.hello_api import HelloResource
from App.apis.user import UsersResource, UserResource

api = Api()


def init_api(app):
    api.init_app(app)


api.add_resource(UsersResource, '/users/')
api.add_resource(UserResource, '/user/<int:id>/')
api.add_resource(HelloResource, '/hello/')
api.add_resource(GoodsListResource, '/goods/')
api.add_resource(GoodsResource, '/goods/<int:id>/', endpoint="single_goods")
