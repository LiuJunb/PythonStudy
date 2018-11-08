# coding:utf-8
from flask import Flask, render_template
from flask_script import Manager # 1.启动命令的管理类

app = Flask(__name__)
# 2.创建Manager管理类
manager = Manager(app)

@app.route('/')
def index():
    return render_template('index.html')

# 4.自定义命令
@manager.command
def hello():
    print "hello"

if __name__ == '__main__':
    # 4.执行脚本管理类
    manager.run()
#   app.run(host='127.0.0.1', port=8000, debug=True)
 

# 测试自定义命令：
# python 13-Flask-Script-CMD.py hello
