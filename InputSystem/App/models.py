# coding: utf-8
# 反响生成models.py文件
# flask-sqlacodegen "mysql://ai_rds_dev:FMAI2020#^%#dev@rm-8vb306n86rr1g506bco.mysql.zhangbei.rds.aliyuncs.com:3306/dev_hj_genealogy" --outfile "/Users/bjhanjia/MyCode/hanjia/录入flask/InputSystem/App/models_copy.py"  --flask
from werkzeug.security import check_password_hash, generate_password_hash

from App.ext import db


class News(db.Model):
    __tablename__ = 'news'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    n_title = db.Column(db.String(16))
    n_content = db.Column(db.String(255))


class Student(db.Model):
    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(25), unique=True)
    _s_pwd = db.Column(db.String(255))
    s_phone = db.Column(db.String(40))

    @property
    def s_pwd(self):
        raise Exception('Error Action:Password not allow to view')

    @s_pwd.setter
    def s_pwd(self, value):
        self._s_pwd = generate_password_hash(value)  # 密码撒盐加密

    def check_password(self, password):
        return check_password_hash(self._s_pwd, password)  # 检验密码的正确


class City(db.Model):
    __tablename__ = 'city'

    id = db.Column(db.Integer, primary_key=True)
    province_id = db.Column(db.Integer, nullable=False)
    city_name = db.Column(db.String(255), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime)


class County(db.Model):
    __tablename__ = 'county'

    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, nullable=False)
    county_name = db.Column(db.String(255), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime)


class Province(db.Model):
    __tablename__ = 'province'

    id = db.Column(db.Integer, primary_key=True)
    province_name = db.Column(db.String(255), nullable=False)
    province_type = db.Column(db.String(255), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime)


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False


class Goods(BaseModel):
    __tablename__ = 'goods'

    g_name = db.Column(db.String(64))
    g_price = db.Column(db.Float, default=0)


class Surname(db.Model):
    __tablename__ = 'surname'

    id = db.Column(db.Integer, primary_key=True)
    name_first = db.Column(db.String(255), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime)
