# coding:utf-8
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# 自定义指令
from flask_migrate import Migrate,MigrateCommand
from flask_script import Shell,Manager

app = Flask(__name__)

# 1.创建数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:rootadmin@127.0.0.1:3306/db_flask2'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

#2.水库扩展/维护类。第一个参数是Flask的实例，第二个参数是Sqlalchemy数据库实例
migrate = Migrate(app,db) 

#3.manager是Flask-Script的实例，这条语句在flask-Script中添加一个db命令
manager = Manager(app)
manager.add_command('db',MigrateCommand)

@app.route('/')
def index():
   
    return 'index page'


#4.定义模型Role
class Role(db.Model):
    # 定义表名
    __tablename__ = 'roles'
    # 定义列对象
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    def __repr__(self):
        return 'Role:'.format(self.name)

#5.定义用户
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    address = db.Column(db.String(64), unique=True, index=True)
    passwrod = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    phone = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return 'User:'.format(self.username)

# 6.运行脚本管理
if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    # app.run()

    manager.run()
    

# 测试步骤：
# 1）先新建一个数据库 db_flask2 和 表
# 2) 执行  python  03-db-weihu.py  db init
# 3）修改数据库的模型

# 4）执行 python 03-db-weihu.py db migrate -m 'add address,not support chine'   数据库会多出一张表( 其实也支持第一次新建表 )
# 5) 执行跟新数据库 python  03-db-weihu.py  db upgrade   对应的表会添加字段

# 6）查看数据库表字段的更新情况     python  03-db-weihu.py  db history  
# 7）返回到指定的某一个历史版本的表  python  03-db-weihu.py  db downgrade 版本号