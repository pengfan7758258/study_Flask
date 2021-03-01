from App.ext import db


class User(db.Model):
    __tablename__ = "ser"  # 指定当前类的ORM映射的表名
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
