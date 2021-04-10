from werkzeug.security import generate_password_hash, check_password_hash

from App.ext import db
from App.models import BaseModel
from App.models.movie_user.model_constant import PERMISSION_NONE

COMMON_USER = 0
BLACK_USER = 1
VIP_USER = 2


class MovieUser(BaseModel):
    username = db.Column(db.String(32), unique=True, nullable=False)
    _password = db.Column(db.String(256), nullable=False)
    phone = db.Column(db.String(32), unique=True, nullable=False)
    is_delete = db.Column(db.Boolean, default=False)
    permission = db.Column(db.Integer, default=PERMISSION_NONE)

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
        # 判断是否是拉黑的用户
        if BLACK_USER & self.permission == BLACK_USER:  # 这里使用的是二进制的方式去做的判断
            return False
        return permission & self.permission == permission  # 不是拉黑用户后判断是否拥有指定权限
