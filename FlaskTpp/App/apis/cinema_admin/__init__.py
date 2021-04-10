from flask_restful import Api

from App.apis.cinema_admin.cinema_address_api import CinemaAddressesResource, CinemaAddressResource
from App.apis.cinema_admin.cinema_hall_api import CinemaHallsResource
from App.apis.cinema_admin.cinema_hall_movie_api import CinemaHallMoviesResource
from App.apis.cinema_admin.cinema_movie_api import CinemaMoviesResource
from App.apis.cinema_admin.cinema_user_api import CinemaUsersResource

cinema_api = Api(prefix='/cinema')

cinema_api.add_resource(CinemaUsersResource, "/users/", strict_slashes=False)

cinema_api.add_resource(CinemaAddressesResource, "/addresses/", strict_slashes=False)
cinema_api.add_resource(CinemaAddressResource, "/address/<int:cinema_id>/", strict_slashes=False)

cinema_api.add_resource(CinemaMoviesResource, "/cinemamovies/", strict_slashes=False)

cinema_api.add_resource(CinemaHallsResource, "/cinemahalls/", strict_slashes=False)

cinema_api.add_resource(CinemaHallMoviesResource, "/cinemahallmovies/", strict_slashes=False)
