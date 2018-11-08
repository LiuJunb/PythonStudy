# coding:utf-8
from . import app_order
from flask import render_template

# 2.给蓝图视图注册路由
@app_order.route('/get_order')
def get_order():
    return 'order page'


@app_order.route('/index')
def index():
    return render_template('order.html')