import json
import os
import random

from flask import Blueprint, request, jsonify, render_template
from flask_mail import Message

from App.ext import cache, mail
from App.models import *
from App.settings import BASE_DIR
from ..utils import *

news_blue = Blueprint("news", __name__)


@news_blue.route('/index/', methods=['GET'])
def index():
    return 'index'


@news_blue.route('/addnews/', strict_slashes=False)
def add_news():
    news = News()
    news.n_title = "周润发 %d" % random.randrange(1000)
    news.n_content = "社会福利 %d" % random.randrange(1000)

    db.session.add(news)
    db.session.commit()
    return "添加新闻成功"


@news_blue.route('/getnewses/', strict_slashes=False)
def get_newses():
    newses = News.query.all()
    # 获取渲染后的内容
    content = render_template('newsContent.html', newses=newses)
    encode_cont_once = myBase64(content)

    encode_cont_spicing = "111111" + encode_cont_once + "222222"
    encode_cont_twice = myBase64(encode_cont_spicing)
    return render_template('newsLIst.html', encode_cont_twice=encode_cont_twice)


@news_blue.route('/getshow/', strict_slashes=False)
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


@news_blue.route('/student/register/', methods=['GET', 'POST'], strict_slashes=False)
def student_register():
    if request.method == "GET":
        return render_template('studentRegister.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        phone = request.form.get('phone')
        code = request.form.get('verify')
        status_code = cache.get(username)
        if code != status_code:
            return 'Fail to register'

        student = Student()
        student.s_name = username
        student.s_pwd = password
        student.s_phone = phone
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

        # username = request.form.get('username')
        # password = request.form.get('password')
        data = json.loads(request.get_data(as_text=True))
        username = data.get('username')
        password = data.get('password')
        student = Student.query.filter(Student.s_name == username).first()
        if student and student.check_password(password):
            return jsonify({'code': 200, 'msg': '登陆成功', 'token': 'abcd'})
        return jsonify({'code': -1, 'msg': '账号或密码错误', 'token': 'abcd'})


@news_blue.route('/sendmail/', strict_slashes=False)
def send_mail():
    msg = Message('FLASK EMAIL', recipients=["pengfan929848421@163.com"])

    msg.body = '哈哈 body'

    msg.html = "<h2>哈哈 html</h2>"

    mail.send(message=msg)

    return "发功邮件成功"


@news_blue.route('/system/province/list/', methods=['POST'], strict_slashes=False)
def zupuProvince():
    data = {'code': 200, 'msg': '查询省份信息'}
    province_list = [{'province_id': province.id, 'province_name': province.province_name} for province in
                     Province.query.all()]
    data['data'] = province_list
    return jsonify(data)


@news_blue.route('/system/city/list/', methods=['POST'], strict_slashes=False)
def zupuCity():
    data = json.loads(request.get_data(as_text=True))
    province_id = data.get('id')
    try:
        province_id = int(province_id)
    except:
        jsonify({'code': -100, 'msg': '参数错误'})
    data = {'code': 200, 'msg': '查询市信息'}
    cities = City.query.filter(City.province_id == province_id)
    city_list = [{'city_id': city.id, 'province_id': city.province_id, 'city_name': city.city_name} for city in
                 cities]
    data['data'] = city_list
    return jsonify(data)


@news_blue.route('/system/county/list/', methods=['POST'], strict_slashes=False)
def zupuCounty():
    data = json.loads(request.get_data(as_text=True))
    city_id = data.get('id')
    try:
        city_id = int(city_id)
    except:
        return jsonify({'code': -100, 'msg': '参数错误'})
    data = {'code': 200, 'msg': '查询区/县信息'}
    counties = County.query.filter(County.city_id == city_id)
    county_list = [{'county_id': county.id, 'city_id': county.city_id, 'county_name': county.county_name} for county in
                   counties]
    data['data'] = county_list

    return jsonify(data)


@news_blue.route('/genealogy/surname/list/', methods=['POST'], strict_slashes=False)
def zupuSurname():
    json_data = json.loads(request.get_data(as_text=True))
    data = {'code': 200, 'msg': '模糊查询姓氏'}
    surname = json_data.get('surname')
    if not surname:
        surnames = Surname.query.all()
        surname_list = [{'surname_id': surnames[i].id, 'value': surnames[i].name_first} for i in
                        range(10)]
    else:
        surnames = Surname.query.filter(Surname.name_first.contains(surname))
        surname_list = [{'surname_id': surname.id, 'value': surname.name_first} for surname in
                        surnames]
    data['data'] = surname_list

    return jsonify(data)


@news_blue.route('/sendcode/', strict_slashes=False)
def send_code():
    username = request.args.get('username')
    phone = request.args.get('phone')

    resp = get_verify_code(phone)

    if resp.json()['code'] == 200:
        obj = resp.json()['obj']
        cache.set(username, obj)

        data = {
            'code': 200,
            'msg': 'success'
        }
        return jsonify(data)

    data = {
        'code': 400,
        'msg': 'fail'
    }
    return jsonify(data)
