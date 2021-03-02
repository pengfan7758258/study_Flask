import random

from flask import Blueprint, render_template

from App.models import db, Student

blue = Blueprint('blue', __name__)


@blue.route('/')
def index():
    return "index"


@blue.route('/addstudent/')
def add_student():
    student = Student()
    student.studentName = "校花%d" % random.randrange(1000)
    student.save()

    return 'Add Success'


@blue.route('/addstudents/')
def add_students():
    students = []
    for i in range(5):
        student = Student()
        student.studentName = '小明%d' % i
        students.append(student)
    db.session.add_all(students)
    db.session.commit()

    return 'Add Students Success'


@blue.route('/getstudent/')
def get_student():
    student = Student.query.first()
    return student.studentName


@blue.route('/getstudents/')
def get_students():
    students = Student.query.all()
    return render_template('index.html', students=students)


@blue.route('/deletestudent/')
def delete_student():
    student = Student.query.first()
    db.session.delete(student)
    db.session.commit()
    return '删除成功'


@blue.route('/updatestudent/')
def update_student():
    student = Student.query.first()
    student.studentName = 'Tom'
    db.session.add(student)
    db.session.commit()
    return '更新成功'
