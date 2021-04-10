from App.ext import db
from App.models import BaseModel
from App.models.cinema_admin import CinemaUser
from App.models.common.movie_model import Movie


class CinemaMovies(BaseModel):
    c_user_id = db.Column(db.Integer, db.ForeignKey(CinemaUser.id))
    movie_id = db.Column(db.Integer, db.ForeignKey(Movie.id))
