import base64
import json
import os
import random
import time

from flask import Blueprint, request, jsonify, render_template
from werkzeug.security import generate_password_hash, check_password_hash

from App.ext import cache
from App.models import *
from App.settings import BASE_DIR

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


@news_blue.route('/getshow/')
def get_encrypt_decrypt():
    t = request.args.get('t')
    try:
        t = int(t)
    except:
        return '2'

    c = time.time() * 1000
    if c > t and c - t < 1000:
        with open(os.path.join(BASE_DIR, 'App/static/js/encrypt_decrypt.js'), 'r', encoding='utf-8') as js_file:
            show_js = js_file.read()

        return show_js
    else:
        return '1'


@news_blue.before_request
def before():
    pass


@news_blue.after_app_request
def after(resp):
    return resp


@news_blue.route('/student/register/', methods=['GET', 'POST'], strict_slashes=False)
def student_register():
    if request.method == "GET":
        return render_template('studentRegister.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        student = Student()
        student.s_name = username
        student.s_pwd = password
        db.session.add(student)
        db.session.commit()
        return 'Success register'


@news_blue.route('/user/login/', methods=['GET', 'POST', 'OPTIONS'], strict_slashes=False)
def student_login():
    if request.method == "GET":
        return render_template('studentLogin.html')
    elif request.method == 'OPTIONS':
        return jsonify({'code': 200, 'msg': '预加载中'})
    else:

        username = request.form.get('username')
        password = request.form.get('password')
        # data = json.loads(request.get_data(as_text=True))
        # username = data.get('username')
        # password = data.get('password')
        student = Student.query.filter(Student.s_name == username).first()
        if student and student.check_password(password):
            return jsonify({'code': 200, 'msg': '登陆成功', 'token': 'abcd'})
        return jsonify({'code': -1, 'msg': '账号或密码错误', 'token': 'abcd'})
