from werkzeug.security import generate_password_hash, check_password_hash

from App.ext import db
from App.models import BaseModel

PERMISSION_NONE = 0  # 公司中离职员工-->如果员工离职把这个改成0还有is_delete设置为True即可
PERMISSION_COMMON = 1  # 普通用户


class AdminUser(BaseModel):
    username = db.Column(db.String(32), unique=True, nullable=False)
    _password = db.Column(db.String(256), nullable=False)
    is_super = db.Column(db.Boolean, default=False)
    is_delete = db.Column(db.Boolean, default=False)
    permission = db.Column(db.Integer, default=PERMISSION_COMMON)

    @property
    def password(self):  # 设置密码，并且不可访问
        raise Exception("Don't access!")

    @password.setter
    def password(self, password_value):  # 密码hash加密
        self._password = generate_password_hash(password_value)

    def check_password(self, pwd):  # 验证密码
        return check_password_hash(self._password, pwd)

    # 验证权限：判断是否拥有指定权限
    def check_permission(self, permission):
        return self.is_super or (permission & self.permission == permission)  # 判断是否拥有指定权限,super用户拥有所有权限
