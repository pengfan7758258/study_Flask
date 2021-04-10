from App.ext import db
from App.models import BaseModel


class Movie(BaseModel):
    __tablename__ = "movies"
    showname = db.Column(db.String(64))  # "梭哈人生"
    shownameen = db.Column(db.String(128))  # "The Drifting Red Balloon"
    director = db.Column(db.String(64))  # "郑来态"
    leadingRole = db.Column(db.String(256))  # "谭佑铭，施子霏，赵韩缨子，孟智超"
    type = db.Column(db.String(64))  # "剧情，爱情，喜剧"
    country = db.Column(db.String(64))  # "中国大陆"
    language = db.Column(db.String(64))  # "汉语普通话"
    duration = db.Column(db.Integer, default=90)  # "90"
    screeningmodel = db.Column(db.String(32))  # "4D"
    openday = db.Column(db.DateTime)  # date("2018-01-30 00:00:00")
    backgroundpicture = db.Column(db.String(256))  # i1/JKLJDLKJFOISDJFOI_.jpg
    flag = db.Column(db.Boolean, default=False)  # 1(可能是1是代表推荐，这个是从淘宝宝拿到的数据格式)
    is_delete = db.Column(db.Boolean, default=False)  # 0
