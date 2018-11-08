# coding:utf-8
from flask import Flask, render_template, make_response, request
app = Flask(__name__)


@app.route('/')
def index():
    resp = make_response('返回给网页的内容')
    # 1.设置cookie,默认有效期是临时cookie,浏览器关闭之后就失效
    resp.set_cookie('cookie_name1','jack1')
    resp.set_cookie('cookie_name2','jack2')
    # 2.max_age 设置有效期，单位：秒
    resp.set_cookie('cookie_name3','jack2', max_age = 3600)

    # 3.使用响应头添加cookie
    resp.headers['Set-Cookie'] ='cookie_name4=jack4; Expires=Tue, 06-Nov-2018 09:50:03 GMT; Max-Age=3600; Path=/'
    return resp

@app.route('/get_cookie')
def get_cookie():
   c= request.cookies.get('cookie_name1')
   return c

@app.route('/del_cookie')
def del_cookie():
   resp =make_response('删除cookie')
   resp.delete_cookie('cookie_name3')  # 设置过期时间为0
   return resp



if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 