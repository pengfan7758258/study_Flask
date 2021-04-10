from flask_restful import Api

from App.apis.movie_user.movie_hall_api import UserMovieHallsResource, UserMovieHallResource
from App.apis.movie_user.movie_order_api import MovieOrdersResource, MovieOrderResource
from App.apis.movie_user.movie_order_pay_api import MovieOrderPayResource
from App.apis.movie_user.movie_user_api import MovieUsersResource

client_api = Api(prefix='/user')  # prefix定义了api模块前缀

client_api.add_resource(MovieUsersResource, '/movieusers/',
                        strict_slashes=False)  # strict_slashes=False在输入路径的最后有没有/都能正常响应

client_api.add_resource(MovieOrdersResource, '/movieorders/', strict_slashes=False)
client_api.add_resource(MovieOrderResource, '/movieorders/<int:order_id>/', strict_slashes=False)

client_api.add_resource(UserMovieHallsResource, '/moviehalls/', strict_slashes=False)
client_api.add_resource(UserMovieHallResource, '/moviehalls/<int:movie_hall_id>/', strict_slashes=False)

client_api.add_resource(MovieOrderPayResource, '/movieorderpay/<int:order_id>/', strict_slashes=False)

