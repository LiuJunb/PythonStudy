# coding:utf-8

from flask import Flask , redirect , url_for, current_app, request

app = Flask(__name__)

# 1.定义一个接口 api
# https://imququ.com/post/four-ways-to-post-data-in-http.html
@app.route('/index', methods = ['POST'])
def index():
    
    # request 中包含了前端发送过来的所有的请求数据
    # 通过request.form可以直接提取请求体中的表单格数的数据，是一个类似字典的对象
    name = request.form.get('name') # 只能拿到同名参数的第一个
    name_lis = request.form.getlist('name') # 拿到同名参数的所有
    print('name_list: %s' % name_lis)
    age = request.form.get('age')

    # 2)获取json数据
    data = request.data
    print('data: %s ' % data)

    # 3)获取查询字符串
    city = request.args.get('city')
    print('city: %s' % city)
    return 'index page name=%s, age=%s' % (name, age)



def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
