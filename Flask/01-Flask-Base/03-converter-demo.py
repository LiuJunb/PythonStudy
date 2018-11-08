# coding:utf-8
from flask import Flask, current_app, redirect, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)

# 1.转换器：<int:goods_id>
# <goods_id> 不加转换器类型，默认使用字符串规则。（除了／字符）
@app.route('/goods/<int:goods_id>')
def goods_detail(goods_id):
    return 'goods detail page %s' % goods_id 

@app.route('/good/<goods_id>')
def good_detail(goods_id):
    return 'good detail page %s' % goods_id 

@app.route('/home')
def home():
    return 'home page'

# 2.自定义转换器
# 1).自定义转换器继承一个基础的转换器
class RegexConverter(BaseConverter):

    def __init__(self, url_map, regex):
        # 调用父类的方法
        super(RegexConverter, self).__init__(url_map)
        # 将正则表达式的参数保存到对象的属性中,flask会去使用这个属性来进行路由的正则匹配
        self.regex = regex

# 2）将自定义的转换器添加到flask框架中
app.url_map.converters['re'] = RegexConverter

# 3)使用自定义转换器
# @app.route("/send/< re (r'1[345678]\d{9}'):mobiles >")
# def send_sms(mobiles):
#     return 'send sms to %s' % mobiles

# 转换器中的冒号 前后不能有空格
# r''代表是后面字符串非转译
# u''代表是后面字符串使用unicode编码
@app.route("/send/<re(r'1[345678]\d{9}'):phone_number>")
def send_sms(phone_number):
    return 'send sms to %s %s' % (phone_number , phone_number)


def main():
    app.run( debug = True )

if __name__ == '__main__':
    main()    
