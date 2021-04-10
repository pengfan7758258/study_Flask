from App.ext import db
from App.models import BaseModel
from App.models.cinema_admin import CinemaUser


class CinemaAddress(BaseModel):
    c_user_id = db.Column(db.Integer, db.ForeignKey(CinemaUser.id))  # 添加电影地址的时候必须在电影用户中存在才能添加（因为外键的关系）
    name = db.Column(db.String(64))  # "深圳戏院影城"
    city = db.Column(db.String(16))  # "深圳"
    district = db.Column(db.String(16))  # "罗湖"
    address = db.Column(db.String(128))  # "罗湖区新园路1号东门步行街西口"
    phone = db.Column(db.String(32))  # "0755-82175808"
    score = db.Column(db.Float, default=10)  # "9.7"
    hallnum = db.Column(db.Integer, default=1)  # "9"
    servicecharge = db.Column(db.Float, default=10)  # "1.2"
    astrict = db.Column(db.Integer, default=20)  # "20"
    flag = db.Column(db.Boolean, default=False)  # 0
    is_delete = db.Column(db.Boolean, default=False)  # 0
