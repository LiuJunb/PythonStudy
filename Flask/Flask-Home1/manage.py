# coding:utf-8
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_session import Session
from flask_wtf import CSRFProtect

app = Flask(__name__)

class Config(object):
    """配置文件"""
    DEBUG = True
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


app.config.from_object(Config)

# 1.创建数据库连接对象
db = SQLAlchemy(app) #  db = SQLAlchemy() ;   db.init_app(app)
# 2.创建redis连接对象（专门做缓存的redis）
redis_store = redis.StrictRedis( host = Config.REDIS_HOST, port = Config.REDIS_PORT )
# 3.利用flask-session，将session数据保存到redis中
Session(app)  # 要配一个专门做session缓存的redis
# 4.给flask补充csrf防护
CSRFProtect(app)


@app.route('/')
def index():
    return 'index page'

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 
