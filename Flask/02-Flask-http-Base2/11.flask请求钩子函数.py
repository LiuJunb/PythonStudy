# coding:utf-8
from flask import Flask, render_template,request
app = Flask(__name__)


@app.route('/')
def index():
    print('index page 执行')
    return 'index page'

@app.route('/home')
def home():
    print('home page 执行')
    return 'index page'

@app.before_first_request
def hande_before_first_request():
    """1.在第一次请求处理之前先被执行"""
    print('hande_before_first_request')  

@app.before_request
def hande_before_request():
    """2.在每次请求之前都被执行"""
    print('hande_before_request')  
    print(request.path)
    

@app.after_request
def hande_after_request(response):
    """3.在每次请求之后被执行,前提是视图函数没有出现异常"""
    print('hande_after_request')   
    # print(request.path)
    return response       

@app.teardown_request
def hande_teardown_request(response):
    """4.在每次请求之后被执行,无论视图函数有没有出现异常(在调试模式不起作用)"""
    print('hande_teardown_request') 
    # print(request.path)
    return response    

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 
