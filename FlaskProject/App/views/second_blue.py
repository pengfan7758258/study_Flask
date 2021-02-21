from flask import Blueprint

second = Blueprint('second', __name__)


@second.route('/hi')
def hello():
    return "Second blue"
