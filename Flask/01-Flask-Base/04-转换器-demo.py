# coding:utf-8
from flask import Flask, current_app, redirect, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# 1.自定义转换器
# 1).自定义转换器继承一个基础的转换器
class MobileConverter(BaseConverter):
    def __init__(self, url_map):
        super(MobileConverter, self).__init__(url_map)
        self.regex = r'1[345678]\d{9}'

    def to_python(self, value):
        print('to_python:',value)  # ('to_python:', u'13234343456')
        return value

    def to_url(self, value):
        print('to_url:',value)  # ('to_url:', '13456778564')
        return value
        

# 2）将自定义的转换器添加到flask框架中
app.url_map.converters['mobile'] = MobileConverter

# 3)使用自定义转换器
@app.route("/send/<mobile:phone_number>")
def send_sms(phone_number):
    return 'send sms to %s' % (phone_number)

# 4)使用自定义转换器
@app.route('/index')
def index():
    url = url_for('send_sms', phone_number = '13456778564')
    # url = '/send/13456778564'
    return redirect(url)

def main():
    app.run( debug = True )

if __name__ == '__main__':
    main()    
