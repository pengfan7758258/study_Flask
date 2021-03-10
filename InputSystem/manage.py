import os

from flask_migrate import MigrateCommand
from flask_script import Manager

from App import create_app

env = os.environ.get('FLASK_ENV', 'default')  # 得到当前的flask的环境是哪一个环境（开发，测试，演示，线上）

app = create_app(env)  # 创建app

manager = Manager(app)  # 创建Manager对象-->能接收命令行参数
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
    from wsgiref.simple_server import make_server
    server = make_server()
    server.serve_forever()
