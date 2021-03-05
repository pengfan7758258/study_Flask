import hashlib


class Student:
    def __init__(self, _password=None):
        self._password = _password

    @property
    def password(self):
        return self._password
        # raise Exception('Error Action')

    @password.setter
    def password(self, value):  # value就是给password设置的值
        self._password = hashlib.new('md5', value.encode('utf-8')).hexdigest()


if __name__ == '__main__':
    student = Student()
    student.password = '123456'
