

import os

from flask_migrate import MigrateCommand
from flask_script import Manager

from App import create_app

env = os.environ.get("FLASK_ENV", 'develop')  # 从环境变量获取env ，判断是什么环境

app = create_app(env)

# 创建Manager对象
manager = Manager(app=app)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    # 使用Manager对象启动app
    manager.run()
