# coding:utf-8
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#1.设置连接数据库的URL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:rootadmin@127.0.0.1:3306/db_flask'

#2.设置每次请求结束后会自动提交数据库中的改动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

#3.查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True

# 4.创建数据库
db = SQLAlchemy(app)

# 5.1创建表
class Role(db.Model):
    # 定义表名
    __tablename__ = 'tbl_roles'
    # 定义列对象
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    # 让Roles表与User表建立关联( 反推User表有一个role属性 )
    user = db.relationship('User', backref='role')

# 5.2创建表
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

@app.route('/')
def index():
    return 'index page'

if __name__ == '__main__':
    # 6.执行创建表的语句
    db.drop_all() 
    db.create_all()

    app.run(host='127.0.0.1', port=8000, debug=True)
 
