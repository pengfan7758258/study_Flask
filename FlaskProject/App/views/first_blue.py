from flask import Blueprint

from App.models import models, User

blue = Blueprint('blue', __name__)


# 主頁路由
@blue.route("/")
def index():
    return "我是蓝图的主页"


# 创建数据库路由
@blue.route('/createdb/')
def createdb():
    models.create_all()
    return '创建数据库成功'


# 删除数据库路由
@blue.route('/dropdb')
def dropdb():
    models.drop_all()
    return "删除数据库成功"


@blue.route('/adduser')
def add_user():
    user = User()
    user.username = 'Tom'

    user.save()

    return '添加用户成功'
