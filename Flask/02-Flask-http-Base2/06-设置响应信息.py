# coding:utf-8
from flask import Flask, render_template, Response
app = Flask(__name__)


@app.route('/index')
def index():
    # 使用元祖的方式，返回响应信息
    #       响应体        状态吗  响应头     
    # return 'index page' , 403,  [ ("City","gz"),("XMG","xmg") ]
    # return 'index page' , '666 customer status des',  [ ("City","gz"),("XMG","xmg") ]
    return 'index page' , '666 customer status des',  {'Name':"jack","Age":12}

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 