# coding:utf-8
from flask import Flask

print ('hello world');
# __name__ : 代表是当前模块的名称
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('user')
def user(self, user_id):
    """这个是视图函数"""
    return 'user'

if __name__ == '__main__':
    app.run(debug=True)