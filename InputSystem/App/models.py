# coding: utf-8
from App.ext import db


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    n_title = db.Column(db.String(16))
    n_content = db.Column(db.String(255))
