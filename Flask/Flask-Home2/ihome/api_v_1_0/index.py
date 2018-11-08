# coding:utf-8
from . import api

@api.route('/')
def admin_index():
    return 'admin_index'


