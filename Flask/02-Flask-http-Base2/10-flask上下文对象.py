# coding:utf-8
from flask import Flask,request, session, g,current_app
app = Flask(__name__)
# request和session都属于请求上下文对象

# current_app和g都属于应用上下文对象

@app.route('/')
def index():
    return 'index'

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 