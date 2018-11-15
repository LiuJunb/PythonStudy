# coding:utf-8
from werkzeug.routing import BaseConverter
from flask import session, jsonify, g
from ihome.utils.response_code import RET
import functools

# 1.自定义一个装饰器login_required
def login_required(view_func):

    # wraps函数的作用是将wrapper内层函数的属性设置为被装饰函数view_func的属性
    @functools.wraps(view_func)
    def wrapper(*args, **kwargs):
        # 1.1判断用户登录状态
        user_id = session.get('user_id')
        # 1.2如果用户登录，执行视图函数
        if user_id is not None:
            # 1.3将用户的id保存到g对象中
            g.user_id = user_id
            return view_func(*args, **kwargs)
        else:
            # 如果未登录，返回未登录的信息
            return jsonify(errno=RET.SESSIONERR, errmsg="用户未登录")

    return wrapper


# 2.装饰器在视图函数中的使用

# @login_required
# def set_user_avatar(user_id):
#     return 'xxx'

    

# set_user_avatar --> wrapper
# set_user_avatar(user_id)--> wrapper(user_id)    












# 1.自定义一个装饰器login_required2
def login_required2(name): # 接受装饰器的参数
    print('1111', name)

    def decorater(view_func):  
        print('2222')

        def wrapper(mobile):  # 接收函数的函数
            print('3333',mobile)
            return view_func(mobile)

        return wrapper

    return decorater



# 2.装饰器在视图函数中的使用
@login_required2('jack')
def set_user_avatar2(text):
    print('44444', text)
    
    return 'xxx'



# set_user_avatar2 --->   wrapper

# set_user_avatar2() --->   wrapper()