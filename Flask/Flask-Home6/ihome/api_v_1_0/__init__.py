# coding:utf-8
from flask import Blueprint
from config import DevelopConfig

print('=======')
# 测试导包
print(DevelopConfig.DEBUG)
print('=======')

# 1.创建蓝图 
# Blueprint必须指定两个参数，api表示蓝图的名称，__name__表示蓝图所在模块
api = Blueprint('api_v_1_0', __name__)

# 2.注册蓝图路由( 点代表相对路径，相对于当前目录 )
# from .index import admin_index
from . import index, verify_ecode, register, profile, house

