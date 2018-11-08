# coding:utf-8
from flask import Flask, render_template, abort, Response
app = Flask(__name__)


@app.route('/index')
def index():
   # 立即终止视图函数的执行，并且可以给前端返回特定的信息
   abort(404) # 返回合法的状态信息

@app.route('/home')
def home():
    # 返回响应头信息
   resp =  Response('403 error page')
   abort(resp)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 