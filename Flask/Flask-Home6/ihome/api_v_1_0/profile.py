# coding:utf-8

# 1.导入蓝图
from . import api
from flask import jsonify, current_app, make_response, request, session, g
# 导入response_code.py中的RET类
from ihome.utils.response_code import RET
# 2.导入ihome.__init__.py中的 redis_store
from ihome import redis_store, db, constants
import re
from ihome.models import User
from sqlalchemy.exc import IntegrityError
from ihome.utils.commons import login_required

@api.route('/users/avatar', methods = ["POST"])
@login_required
def set_user_avatar():
   """
    设置用户头像
    多媒体表单参数：图片， 用户id
   """
   user_id = g.user_id
   print(user_id)
    
   # 1.获取图片
   image_file = request.files.get('avatar')

   if image_file is None:
        return jsonify(errno=RET.PARAMERR, errmsg="未上传图片")
        
   file_name =  image_file.filename
   print(file_name)
   image_data = image_file.read()
   file_url =  './ihome/static/upload/'+str(user_id)+file_name
   try:
       with open(file_url, 'wb') as f:
            f.write(image_data)
   except Exception as e:
       return jsonify(errno =RET.IOERR, errmsg = "图片上传失败") 
  

   avatar_url = 'http://127.0.0.1:5000/static/upload/'+str(user_id)+file_name
   # 将头像保存到数据库中
   try:
        User.query.filter_by(id=user_id).update({"avatar_url": avatar_url})
        db.session.commit()
   except Exception as e:
       db.session.rollback()
       current_app.logger.error(e)
       return jsonify(errno =RET.DBERR, errmsg = "图片存储失败")

   return jsonify(errno =RET.OK, errmsg = "保存成功", data={'avatar_url':avatar_url}) 



   
@api.route("/user", methods=["GET"])
@login_required
def get_user_profile():
    """获取个人信息"""
    user_id = g.user_id
    # 查询数据库获取个人信息
    try:
        user = User.query.get(user_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="获取用户信息失败")

    if user is None:
        return jsonify(errno=RET.NODATA, errmsg="无效操作")

    return jsonify(errno=RET.OK, errmsg="OK", data=user.to_dict())



@api.route('/users/name', methods = ['PUT'])
@login_required
def change_user_name():
    """
        修改用户名
    """
    user_id = g.user_id

    req_data = request.get_json()
    if not req_data:
        return jsonify(errno=RET.PARAMERR, errmsg ="参数不完整" )

    name = req_data.get('name')
    if not name:
        return jsonify(errno=RET.PARAMERR, errmsg ="名字不能为空" )

    # 更新数据库的用户名
    print(req_data)  # {u'name': u'18312016879'}
    print(name) # 18312016879

    try:
        # name是唯一性的
        User.query.filter_by(id=user_id).update({"name":name})
        db.session.commit()
    except IndentationError as e:
        db.session.rollback()
        current_app.logger.error(e)
        return jsonify(errno= RET.DBERR , errmsg = "用户名已经存在")    
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)
        return jsonify(errno= RET.DBERR , errmsg = "用户名修改错误")

    # 修改完成用户名之后，将用户名存在session中
    session['name'] = name
    return jsonify( errno=RET.OK, errmsg = "OK", data={"name":name} )  


@api.route('/users/auth', methods = ["POST"])
@login_required
def set_user_auth():
    """
        保存实名认真信息
    """
    user_id = g.user_id

    # 1.获取参数
    req_data = request.get_json()

    if not req_data:
        return jsonify(errno= RET.PARAMERR, errmsg="参数错误")

    real_name = req_data.get('real_name')
    id_card = req_data.get('id_card')
    print(real_name, id_card) # (u'\u5218\u519b', u'1212121212121212')
    
    # 2.参数校验
    if not all([real_name, id_card]):
        return jsonify(errno= RET.PARAMERR, errmsg="参数错误")

    # 3.保存用户名和密码
    try:
        User.query.filter_by(id=user_id, real_name=None, id_card=None)\
            .update({"real_name":real_name,"id_card":id_card})
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="保存数据库失败")

    return jsonify(errno=RET.OK, errmsg="OK")



@api.route('/users/auth', methods=['GET'])
@login_required
def get_user_auth():

    user_id = g.user_id

    try:
        # 通过主键从数据库获取
        user = User.query.get(user_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="获取用户实名信息失败")

    if user is None:
        return jsonify(errno=RET.NODATA, errmsg="无效操作")

    return jsonify(errno=RET.OK, errmsg="OK", data=user.auth_to_dict())    
    