# coding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_session import Session
from flask_wtf import CSRFProtect

import logging
from logging.handlers import RotatingFileHandler
# from ihome.utils.commons import ReConverter

from config import config_map
from ihome.utils import ReConverter

# 1.创建数据库连接对象
db = SQLAlchemy()
# 2.定义redis连接对象（共外部使用）
redis_store = None

# from ihome import api_v_1_0 
# from . import api_v_1_0  # 这个代码不能放在db 初始化之前调用，对导致循环引用（放在这里可以）

# 配置日志信息
# 设置日志的记录等级( INFO会把 info warn erro 记录在文件中 )
logging.basicConfig(level=logging.INFO)
# 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小100M、保存的日志文件个数上限
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)
# 创建日志记录的格式                 日志等级    输入日志信息的文件名 行数    日志信息
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象（flask app使用的）添加日记录器
logging.getLogger().addHandler(file_log_handler)

# 使用案例：logging.debug('')  logging.info('')  logging.warn('warn')  logging.error('error')  会写到logs文件中
# import logging
# from flask import current_app
# current_app.logger.info('') 

def create_app(config_name):
    logging.error('000000000') 
    
    """
        创建app的工厂类
    """
    app = Flask(__name__)
    
    config_class = config_map.get(config_name)
    app.config.from_object(config_class)
     
    # 据库连接对象 绑定 创建好的app
    db.init_app(app)

    # 2.创建redis连接对象（专门做缓存的redis）
    global redis_store
    redis_store = redis.StrictRedis(
        host=config_class.REDIS_HOST, port=config_class.REDIS_PORT)
    # 3.利用flask-session，将session数据保存到redis中
    Session(app)  # 要配一个专门做session缓存的redis
    # 4.给flask补充csrf防护
    # CSRFProtect(app)

    # 注册自定义路由的正则转化器
    app.url_map.converters['re'] = ReConverter

    # 5.注册蓝图( api 是蓝图的名称)
    from . import api_v_1_0, web_html  # 推迟导入
    app.register_blueprint(api_v_1_0.api, url_prefix='/api/v1_0')
    app.register_blueprint(web_html.html)
    
    return app