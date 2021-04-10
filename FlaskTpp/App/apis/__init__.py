from App.apis.admin import admin_api
from App.apis.common import common_api
from App.apis.cinema_admin import cinema_api
from App.apis.movie_user import client_api


def init_apis(app):
    client_api.init_app(app)
    cinema_api.init_app(app)
    admin_api.init_app(app)
    common_api.init_app(app)
