# 告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码
# coding:utf-8
from flask import Flask,current_app
import demo__name__;  # 1.打印当前模块的名称( demo__name__ )

# /Users/android-school/Python/myPython2Env/bin/python

print (__name__)  # 打印当前模块的名称( __main__ )
# 2.__name__ : 代表是当前模块的名称
app = Flask(__name__,
            static_url_path="/python",  # 指定静态资源的url的前缀，默认是static
            static_folder="static",
            template_folder="templates")   #  指定静态文件的目录，默认是static  
#app = Flask('__main__')
#app = Flask('abck')

# 3.配置文件的使用
# 1).第一种导入配置
#app.config.from_pyfile('config.cfg')

# 2).第二种导入配置（通过类）
class Config(object):
    DEBUG = True
    # 添加自定义的配置变量
    XMG = 'xiaomage'

app.config.from_object(Config)

# 3).第三种导入配置
# app.config['DEBUG'] = True

# 4.第四种导入配置
# app.config.update( key1 = vaule, key2 = vaule )

@app.route('/')
def index():
    # 1 / 0;
    # 4.读取自定义的配置变量 
    # 1)通过app获取
    print (app.config.get('XMG'))
    # 2）通过current_app 获取
    print (current_app.config.get('XMG'))

    return '<h1>Hello World!</h1>'

@app.route('/user')
def user(self, user_id):
    """这个是视图函数"""
    return 'user'

if __name__ == '__main__':
    # app.run()
    # app.run(debug=True)
    app.run( host='0.0.0.0', port=8000)