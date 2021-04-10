from App.ext import db
from App.models import BaseModel
from App.models.cinema_admin import CinemaAddress


class Hall(BaseModel):
    h_address_id = db.Column(db.Integer, db.ForeignKey(CinemaAddress.id))  # 放映厅所在的影院地址
    h_num = db.Column(db.Integer, default=1)  # 放映厅编号
    h_seats = db.Column(db.String(128))  # 放映厅座位
