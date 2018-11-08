# coding:utf-8
from flask import Blueprint


# 1.创建蓝图( 先在大的templates范围找，在到小templates范围找 )
app_order = Blueprint('app_order',__name__,template_folder='templates')

# 2.注册视图
# @app_order.route('/get_order')
# def get_order():
#     return 'order page'

from .views import get_order