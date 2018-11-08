# coding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_session import Session
from flask_wtf import CSRFProtect

# from ihome import api_v_1_0
from . import api_v_1_0
from config import config_map


# 1.创建数据库连接对象
db = SQLAlchemy()
# 2.定义redis连接对象（共外部使用）
redis_store = None

def create_app(config_name):
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
    redis_store = redis.StrictRedis( host = config_class.REDIS_HOST, port = config_class.REDIS_PORT )
    # 3.利用flask-session，将session数据保存到redis中
    Session(app)  # 要配一个专门做session缓存的redis
    # 4.给flask补充csrf防护
    CSRFProtect(app)
    # 5.注册蓝图( api 是蓝图的名称)
    app.register_blueprint(api_v_1_0.api, url_prefix = '/api/v1.0')
    return app