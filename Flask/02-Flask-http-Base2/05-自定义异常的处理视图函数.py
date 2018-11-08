# coding:utf-8
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/index')
def index():
    pass

@app.errorhandler(404)
def error_404_handler(err):
    return u"出现404错误: %s " % err
   



if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 