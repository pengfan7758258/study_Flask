import os

from flask_migrate import MigrateCommand
from flask_script import Manager

from App import create_app

env = os.environ.get('FLASK_ENV', "default")  # 获取开发环境类别（开发,测试，演示，线上）
app = create_app(env)  # 创建app
manager = Manager(app)  # 可以使用命令去运行项目
manager.add_command('db', MigrateCommand)  # 可以使用迁移命令

if __name__ == '__main__':
    manager.run()  # 最终调用的还是app.run()-->不过可以把终端命令当中的参数传递进去
