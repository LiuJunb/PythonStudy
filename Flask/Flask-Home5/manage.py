# coding:utf-8
from ihome import create_app, db
# 数据库管理命令
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = create_app('develop')

# 导入要创建的表
from ihome import models

manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
  # app.run(host='127.0.0.1', port=8000, debug=True)
  manager.run()  # python manage.py runserver
