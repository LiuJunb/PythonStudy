# coding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:rootadmin@127.0.0.1:3306/db_flask'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True

# 1.配置数据库的连接
app.config.from_object(Config)    


# 2.新建数据库操作对象
db = SQLAlchemy(app)

# 3.1创建表
class Role(db.Model):
    # 定义表名
    __tablename__ = 'tbl_roles'
    # 定义列对象
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    # 让Roles表与User表建立关联( 反推User表有一个role属性 )
    user = db.relationship('User', backref='role')

# 3.2创建表
class User(db.Model):
    # 定义表名
    __tablename__ = 'tbl_user'
    # 定义列的字段
    id = db.Column( db.Integer, primary_key=True )
    name = db.Column( db.String(64), unique=True )
    email = db.Column(db.String(64),unique=True)
    pswd = db.Column(db.String(64))
    
    # 定义外键
    role_id = db.Column(db.Integer, db.ForeignKey('tbl_roles.id'))
    # role


if __name__ == '__main__':
    # 6.执行创建表的语句
    db.drop_all() 
    db.create_all()

    app.run(host='127.0.0.1', port=8000, debug=True)
 
