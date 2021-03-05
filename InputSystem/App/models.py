# coding: utf-8
from werkzeug.security import check_password_hash, generate_password_hash

from App.ext import db


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    n_title = db.Column(db.String(16))
    n_content = db.Column(db.String(255))


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(25), unique=True)
    _s_pwd = db.Column(db.String(255))

    @property
    def s_pwd(self):
        raise Exception('Error Action:Password not allow to view')

    @s_pwd.setter
    def s_pwd(self, value):
        self._s_pwd = generate_password_hash(value)

    def check_password(self, password):
        return check_password_hash(self._s_pwd, password)
