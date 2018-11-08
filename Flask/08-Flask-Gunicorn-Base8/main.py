# coding:utf-8
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return 'index page'

# if __name__ == '__main__':
#   app.run()  # 可有可无
 
 # -w 启动的进程数; 
 # -b 指定ip和端口；
 # --access-logfile指定日志文件存储的路径；  
 # main:app 指定要运行的py文件 和 app
 # ( 注意要新家一个logs文件 )

 # gunicorn -w 4 -b 127.0.0.1:8000 --access-logfile ./logs/log main:app
 # gunicorn -w 4 -b 127.0.0.1:8000 -D --access-logfile ./logs/log main:app
 
 # 90069   0.0  0.2  2477776  15620   ??  S     1:11下午   0:00.11
 # kill -9 【 进程id: 90069 】