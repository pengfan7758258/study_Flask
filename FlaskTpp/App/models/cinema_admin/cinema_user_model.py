from werkzeug.security import generate_password_hash, check_password_hash

from App.ext import db
from App.models import BaseModel


class CinemaUser(BaseModel):
    username = db.Column(db.String(32), unique=True, nullable=False)
    _password = db.Column(db.String(256), nullable=False)
    phone = db.Column(db.String(32), unique=True, nullable=False)
    is_delete = db.Column(db.Boolean, default=False)
    is_verify = db.Column(db.Boolean, default=False)

    @property
    def password(self):  # 设置密码，并且不可访问
        raise Exception("Don't access!")

    @password.setter
    def password(self, password_value):  # 密码hash加密
        self._password = generate_password_hash(password_value)

    def check_password(self, pwd):  # 验证密码
        return check_password_hash(self._password, pwd)

    def check_permission(self, permission):  # 验证权限
        if not self.is_verify:  # 查看当前电影用户是否被后台管理认证
            return False
        c_u_permissions = CinemaUserPermission.query.filter_by(c_user_id=self.id)  # 获取当前电影院用户所拥有的所有权限

        for user_permission in c_u_permissions:
            if CinemaPermission.query.get(user_permission.cp_id).cp_name == permission:
                return True

        return False


class CinemaPermission(BaseModel):
    cp_name = db.Column(db.String(64), unique=True)


class CinemaUserPermission(BaseModel):
    c_user_id = db.Column(db.Integer, db.ForeignKey(CinemaUser.id))
    cp_id = db.Column(db.Integer, db.ForeignKey(CinemaPermission.id))
