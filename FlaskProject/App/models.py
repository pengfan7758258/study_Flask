from flask_sqlalchemy import SQLAlchemy

from App.ext import models


class User(models.Model):
    id = models.Column(models.Integer, primary_key=True)  # 主键默认自增
    username = models.Column(models.String(16))
    
    def save(self):
        models.session.add(self)
        models.session.commit()