# coding:utf-8
from flask import Blueprint

# 1.创建蓝天对象
# Blueprint必须指定两个参数，admin表示蓝图的名称，__name__表示蓝图所在模块
app_orders = Blueprint('app_order',__name__)

# 2.注册蓝图路由
@app_orders.route('/get_order')
def get_order():
    return 'get_order page'

