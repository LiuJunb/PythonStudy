# coding:utf-8
from flask import Flask, render_template, jsonify
import json
app = Flask(__name__)


@app.route('/')
def index():
    # 1.定义一个字典
    data = {
        "name": 'jack',
        "age": 20
    }
    # 2.字典转json
    str = json.dumps(data)  # 字典转json
    return str, 200 , {'Content-Type':'application/json'} 

@app.route('/home')
def home():
    # 1.定义一个字典
    data = {
        "name": 'jack',
        "age": 20
    }
    # 2.字典转json, 并且添加响应头
    return jsonify(data) 


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 