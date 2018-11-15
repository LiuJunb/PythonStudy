# coding:utf-8
from flask import Blueprint, current_app , make_response
from flask_wtf import csrf
# 1.创建蓝图 
# Blueprint必须指定两个参数，api表示蓝图的名称，__name__表示蓝图所在模块
html = Blueprint('web_html',__name__)

# 2.注册蓝图路由( 点代表相对路径，相对于当前目录 )
# from .index import admin_index
# from . import index


# http://127.0.0.1:5000
# http://127.0.0.1:5000/index.html
# http://127.0.0.1:5000/register.html
@html.route("/<re(r'.*'):html_file_name>")
def get_html(html_file_name):

    # 如果 html_file_name 为 “”，表示访问的路径是 ／ ,请求的是主页
    if not html_file_name:
        html_file_name = 'index.html'

    if html_file_name != 'favicon.ico':
        html_file_name = 'html/' + html_file_name

    # flask 提供返回的静态方法 
    # return current_app.send_static_file(html_file_name)

    # 1.生成csrf字符窜
    csrf_token = csrf.generate_csrf()
    # 2.把csrf_token添加到cookie中
    resp =make_response( current_app.send_static_file(html_file_name) )
    resp.set_cookie('csrf_token', csrf_token)
    return resp



