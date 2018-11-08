# coding:utf-8
from flask import Blueprint


# 1.创建蓝图
app_order = Blueprint('app_order',__name__)

# 2.注册视图
# @app_order.route('/get_order')
# def get_order():
#     return 'order page'

from .views import get_order