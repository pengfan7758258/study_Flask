from flask import Blueprint

from App.models import db

blue = Blueprint('blue', __name__)


@blue.route('/')
def index():
    return "index"


@blue.route('/create/')
def create():
    db.create_all()
    return '创建成功'


@blue.route('/drop/')
def drop():
    db.drop_all()
    return '删除成功'
