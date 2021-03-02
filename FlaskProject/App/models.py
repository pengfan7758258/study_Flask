from App.ext import db


class User(db.Model):
    __tablename__ = "user"  # 指定当前类的ORM映射的表名
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))


class Student(db.Model):
    __tablename__ = "student"  # 指定当前类的ORM映射的表名
    id = db.Column(db.Integer, primary_key=True)
    studentName = db.Column(db.String(20))

    def save(self):
        db.session.add(self)
        db.session.commit()
