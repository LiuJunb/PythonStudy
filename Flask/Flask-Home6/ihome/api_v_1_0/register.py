# coding:utf-8

# 1.导入蓝图
from . import api
from flask import jsonify, current_app, make_response, request, session
# 导入response_code.py中的RET类
from ihome.utils.response_code import RET
# 2.导入ihome.__init__.py中的 redis_store
from ihome import redis_store, db, constants
import re
from ihome.models import User
from sqlalchemy.exc import IntegrityError

# post 方法 前端还要添加 crsf_token 和 cookie 中也要crsf_token
@api.route('/users', methods=['POST'])
def register():
   """
    手机号  密码
   """
   req_dict = request.get_json()
   mobile = req_dict.get('mobile')
   password = req_dict.get('password')
   password2 = req_dict.get('password2')
   print(mobile, password, password2)
    
   if not all([mobile, password, password2]):
       return jsonify(errno = RET.PARAMERR, errmsg = '参数不完整')

   if not re.match(r"1[345678]\d{9}", mobile):
       return jsonify(errno = RET.PARAMERR, errmsg = "手机号格式错误")

   if password != password2:
        return jsonify( errno= RET.PARAMERR, errmsg = "两次输入的密码不一致" )

   user = User(name=mobile, mobile=mobile)

   # 对密码的加密：使用sha256算法加密 
   # pbkdf2:sha256:50000   $  cK0U6uNi  $  7ff2b0e361172433e8d391b3865a35d5cf252a30db0f3bf42b0f719771430225
   user.password = password

   try:
        db.session.add(user)
        db.session.commit()
   except IntegrityError as e:
        db.session.rollback()
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAEXIST , errmsg='手机号已经存在')
   except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR , errmsg='数据库查询出错')

   # 在session中保存用户的数据，相当于登录状态
   session['name'] = mobile
   session['mobile'] = mobile
   session['user_id'] = user.id

   return jsonify(errno=RET.OK, errmsg= "注册成功")



# post 方法要注意crsf验证机制
@api.route("/sessions", methods=['POST'])
def login():
    """
        用户登录
        参数：手机号 和 密码
    """
    req_dict = request.get_json()

    mobile = req_dict.get('mobile')
    password = req_dict.get('password')

    if not all([mobile, password]):
        return jsonify(errno = RET.PARAMERR, errmsg = "参数不完整")

    if not re.match(r"1[345678]\d{9}", mobile) :
        return jsonify(errno = RET.PARAMERR, errmsg = "手机号码错误")

    # 判断错误的次数是否超过限制，如果超过限制，则返回
    # redis 记录 ： ‘assess_nums_请求的ip’ 
    user_ip = request.remote_addr # 获取客户端的IP

    try:
        assess_nums = redis_store.get("access_num_%s" % user_ip)
    except Exception as e:
        current_app.logger.error(e)   
    else:
        if assess_nums is not None and int(assess_nums) >= constants.LOGIN_ERROR_MAX_TIMES:
            return jsonify(errno = RET.REQERR, errmsg = "错误次数过多，请稍后重试")

    try:
        user = User.query.filter_by(mobile = mobile).first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify( errno = RET.DBERR, errmsg = "获取用户信息失败" )

    if user is None or not user.check_password(password):
        try:
            redis_store.incr('access_num_%s' % user_ip)
            redis_store.expire('access_num_%s' % user_ip , constants.LOGIN_ERROR_MAX_TIMES)
        except Exception as e:
            current_app.logger.error(e)
        return jsonify(errno = RET.DATAERR, errmsg = "用户名或密码错误")    
        
    session['name'] = mobile
    session['mobile'] = mobile
    session['user_id'] = user.id

    return jsonify(errno= RET.OK, errmsg = "登录成功")

@api.route("/session", methods=["GET"])
def check_login():
    """检查登录状态"""
    name = session.get('name')
    if name is not None:
        return jsonify(errno=RET.OK, errmsg="true", data={"name":name})
    else:
        return jsonify(errno=RET.SESSIONERR, errmsg="false")   

@api.route("/session", methods=["DELETE"])
def out_login():
    """检查退出登录"""
    session.clear()
    return jsonify(errno=RET.OK, errmsg="ok")




