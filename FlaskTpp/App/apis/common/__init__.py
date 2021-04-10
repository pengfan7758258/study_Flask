from flask_restful import Api

from App.apis.common.city_api import CitiesResource
from App.apis.common.movie_api import MoviesResource, MovieResource

common_api = Api(prefix='/common')

common_api.add_resource(CitiesResource, '/cities/', strict_slashes=False)
common_api.add_resource(MoviesResource, '/movies/', strict_slashes=False)
common_api.add_resource(MovieResource, '/movie/<int:movie_id>', strict_slashes=False)
