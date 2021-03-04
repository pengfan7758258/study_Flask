import base64
import random

from flask import Blueprint, request, jsonify, render_template

from App.ext import cache
from App.models import *

news_blue = Blueprint("news", __name__)


def myBase64(mstr):
    encode_mstr = base64.standard_b64encode(mstr.encode('utf-8')).decode('utf-8')
    return encode_mstr


@news_blue.route('/index/', methods=['GET'])
def index():
    return 'index'


@news_blue.route('/addnews/')
def add_news():
    news = News()
    news.n_title = "周润发 %d" % random.randrange(1000)
    news.n_content = "社会福利 %d" % random.randrange(1000)

    db.session.add(news)
    db.session.commit()
    return "添加新闻成功"


@news_blue.route('/getnewses/')
def get_newses():
    newses = News.query.all()
    # 获取渲染后的内容
    content = render_template('newsContent.html', newses=newses)
    encode_cont_once = myBase64(content)

    encode_cont_spicing = "111111" + encode_cont_once + "222222"
    encode_cont_twice = myBase64(encode_cont_spicing)

    return render_template('newsLIst.html', encode_cont_twice=encode_cont_twice)
