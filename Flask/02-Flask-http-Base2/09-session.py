# coding:utf-8
from flask import Flask, render_template, session
app = Flask(__name__)

# 2.设置session的key
app.config['SECRET_KEY'] ='sdfsdfsfgdffg'

@app.route('/')
def index():
    # 1.设置session( Django默认把session保存到mysql;flask把数据加密后保存到前端的cookie )
    # 扩展：session可以保存在程序的内存中，文件中，数据库中，redis中,cookie中...
    session['name'] = 'jack'    
    session['mobile'] = '186342345435'    
    return 'index page login success'

@app.route('/home')
def home():
    # 3.获取session
    mobile = session.get('mobile'); 
    return 'session: % s' % mobile


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 
