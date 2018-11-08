# coding:utf-8
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


@app.route('/',methods=['POST'])
def index():
    username = request.form.get('username')
    password = request.form.get('password')

    if not all([username, password]):
        res = {
            "code":1,
            "msg" :'invalid params'
        }
        return jsonify(res)

    if username == 'xmg' and password == '123':
        res = {
            "code":0,
            "msg" :'invalid params'
        }
        return jsonify(res)
    else:
        res = {
            "code":2,
            "msg" :'username or password wrong'
        }
        return jsonify(res)
    # return render_template('index.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 
