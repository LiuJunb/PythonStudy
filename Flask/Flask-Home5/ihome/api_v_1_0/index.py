# coding:utf-8
from . import api
from ihome import db

# 导入打印日志的api
import logging
from flask import current_app

@api.route('/')
def admin_index():

    current_app.logger.info('hshsh')

    return 'admin_index'


