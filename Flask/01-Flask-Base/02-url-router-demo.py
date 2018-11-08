# coding:utf-8

from flask import Flask,current_app,redirect,url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'hellow'

@app.route('/post_only', methods = ['POST','GET'])
def post_only():
    return 'post_only'

@app.route('/hello', methods = ['POST'])
def hello1():
    return 'hello 1'

@app.route('/hello', methods = ['GET'])
def hello2():
    return 'hello 2'


@app.route('/hi1')
@app.route('/hi2')
def h1():
    return 'hi page'

@app.route('/login')
def login():
    # 使用url__for的函数通过视图函数的名称找到路由
    # url = url_for('index')
    url = '/'
    return redirect(url)


def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()    

