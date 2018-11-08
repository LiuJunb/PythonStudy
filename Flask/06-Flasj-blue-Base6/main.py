# coding:utf-8
from flask import Flask, render_template
from order import app_order
app = Flask(__name__)


# 3.在app程序中注册蓝图
app.register_blueprint(app_order, url_prefix = '/orders')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    print(app.url_map)
    app.run(host='127.0.0.1', port=8000, debug=True)
 
