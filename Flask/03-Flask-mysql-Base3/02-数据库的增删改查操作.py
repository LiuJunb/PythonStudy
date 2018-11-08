# coding:utf-8
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#1.设置连接数据库的URL( 先要手动创建好数据才能链接 )
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:rootadmin@127.0.0.1:3306/db_flask'

#2.设置每次请求结束后会自动提交数据库中的改动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

#3.查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True


# 4.创建数据库操作对象
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

    #repr()方法显示一个可读字符串
    def __repr__(self):
        return 'Role:%s' % self.name

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

@app.route('/create')
def create():
    db.drop_all() 
    db.create_all()
    return 'create page'


@app.route('/add')
def add():
    # 6.数据库的增删改查操作
    # 6.1 添加数据
    ro1 = Role(name='admin')
    ro2 = Role(name='user')
    db.session.add(ro1)
    # db.session.commit()
    db.session.add_all([ro2])
    db.session.commit()

    us1 = User(name='wang',email='wang@163.com',pswd='123456',role_id=ro1.id)
    us2 = User(name='zhang',email='zhang@189.com',pswd='201512',role_id=ro2.id)
    us3 = User(name='chen',email='chen@126.com',pswd='987654',role_id=ro2.id)
    us4 = User(name='zhou',email='zhou@163.com',pswd='456789',role_id=ro1.id)
    db.session.add_all([us1,us2,us3,us4])
    db.session.commit()

    return 'index page'


@app.route('/delete')
def delete():

    return 'delete page'

@app.route('/update')
def update():

    return 'update page'


@app.route('/query')
def query():
    lis =Role.query.all()
    print(lis[0].name)
    print(lis[1].name)
    print('=========1========')
    role=db.session.query(Role).first()
    print(role.name, role.id)
    print('=========2========')
    print(role.user)
    print('=========3========')
    

    

    return 'query page'

if __name__ == '__main__':

    app.run(host='127.0.0.1', port=8000, debug=True)
 
