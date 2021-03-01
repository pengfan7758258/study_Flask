import os

from flask_script import Manager

from App import create_app

env = os.environ.get('FLASK_ENV', 'default')  # 导入环境，判断使用哪个环境

app = create_app(env)  # 创建app

manager = Manager(app)  # 可以使用命令cmd去运行程序，并且支持动态传参

if __name__ == '__main__':
    manager.run()
