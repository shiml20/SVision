from flask_script import Manager, Server  # 管理项目 指定额外命令
from flask_migrate import MigrateCommand  # 管理数据库需要的脚本
from myApp import create_app

# 1. 利用工厂函数生成APP
app = create_app()
# 2. 创建manager 管理app的对象
manager = Manager(app)
# 3. 给管理对象中添加命令
manager.add_command('runserver', Server(host='0.0.0.0'))
manager.add_command('db', MigrateCommand)  # 绑定额外的db命令

"""
python manage.py runserver
python manage.py db init #初始化
python manage.py db migrate -m "message" #提交变更
python manage.py db upgrade #升级变更
python manage.py db downgrade #降级变更
"""
if __name__ == '__main__':
    manager.run()
