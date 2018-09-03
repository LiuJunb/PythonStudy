from flask import Flask, g

from redisclient import RedisClient

__all__ = ['app']
# 这里声明了Flask对象
app = Flask(__name__)


def get_conn():
    if not hasattr(g, 'redis'):
        g.redis = RedisClient()
    return g.redis


# 首页接口
@app.route('/')
def index():
    return '<h2>Welcome to Proxy Pool System</h2>'


# 获取随机代理接口
@app.route('/random')
def get_proxy():
    """
    Get a proxy
    :return: 随机代理
    """
    conn = get_conn()
    return conn.random()


# 获取代理池总量接口
@app.route('/count')
def get_counts():
    """
    Get the count of proxies
    :return: 代理池总量
    """
    conn = get_conn()
    return str(conn.count())


if __name__ == '__main__':
    app.run()
