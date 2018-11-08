# coding:utf-8
from flask import Flask, render_template
# 倒入蓝图
from order import app_orders
# 1.循环引用-解决方案1-推迟一方的加载
# from user import get_user
from goods import get_goods

app = Flask(__name__)

# 2.循环引用-解决方案2-使用装饰器
app.route('/get_goods')(get_goods)

# 3.在app程序中注册蓝图
app.register_blueprint(app_orders, url_prefix='/orders')

@app.route('/')
def index():
    # 2.1推迟一方的加载
    # from user import get_user
    return 'index page'

if __name__ == '__main__':
  print(app.url_map)
  app.run(host='127.0.0.1', port=8000, debug=True)
 