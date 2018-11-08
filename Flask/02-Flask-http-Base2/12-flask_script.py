# coding:utf-8
from flask import Flask, render_template
from flask_script import Manager # 1.启动命令的管理类

app = Flask(__name__)
# 2.创建Manager管理类
manager = Manager(app)

@app.route('/')
def index():
    return "index page"

if __name__ == '__main__':
  # 3.执行脚本管理类
  manager.run()
 
