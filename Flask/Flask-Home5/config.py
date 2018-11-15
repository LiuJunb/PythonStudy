# coding:utf-8
import redis

class Config(object):
    """配置文件"""
    SECRET_KEY = 'flask_home'

    # 1.数据库的配置文件
    SQLALCHEMY_DATABASE_URI = 'mysql://root:rootadmin@127.0.0.1:3306/flask_home'
    #SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    #SQLALCHEMY_ECHO = True

    # 2.redis 配置文件
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # 3.Flask-Session 配置
    SESSION_TYPE = 'redis'  # 指定session存放到哪里
    # 指定session存放的服务器（独立一个服务器，实际应该与上面的不一样）
    SESSION_REDIS = redis.StrictRedis(host = REDIS_HOST, port = REDIS_PORT)
    SESSION_USE_SIGNER = True # 对session中的key进行隐藏
    PERMANENT_SESSION_LIFETIME = 86400 # session 设置有效时间一天,单位秒


class DevelopConfig(Config):
    DEBUG = True
    pass


class ProductConfig(Config):
    pass    

# 定一个字典
config_map = {
    "develop": DevelopConfig,
    "product": ProductConfig,
}    