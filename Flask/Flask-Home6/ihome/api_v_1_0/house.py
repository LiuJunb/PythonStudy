# coding:utf-8

# 1.导入蓝图
from . import api
from flask import jsonify, current_app, make_response, request, session, g
# 导入response_code.py中的RET类
from ihome.utils.response_code import RET
# 2.导入ihome.__init__.py中的 redis_store
from ihome import redis_store, db, constants
import re
from ihome.models import User, Area, House, Facility, HouseImage
from sqlalchemy.exc import IntegrityError
from ihome.utils.commons import login_required
import json

@api.route('/areas', methods = ["GET"])
def get_areas():
    """
        获取城区的接口，这个接口的数据会经常请求，并且变化不大，可以缓存起来
    """

    try:
        resp_json=redis_store.get('area_info')
    except Exception as e:
        current_app.logger.error(e)
    else:
        if resp_json is not None:
           current_app.logger.info('缓存中获取')
           return resp_json, 200, {'Content-Type':'application/json'}

    try:
        areas = Area.query.all()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno = RET.DBERR, errmsg = "数据库操作失败")

    a_dict_lis = []
    for area in areas:
        a_dict_lis.append( area.to_dict() )

    # 将返回的数据转成json字符串, dict() 构建一个字典
    resp_dict = dict(errno = RET.OK, errmsg = "获取城区成功", data = a_dict_lis)  
    resp_json=json.dumps(resp_dict)
    # 将数据保存到 内存缓存的数据库 redis 中
    try:
        redis_store.setex("area_info", constants.AREA_INFO_REDIS_CACHE_EXPIRES, resp_json)
    except Exception as e:
        current_app.logger.error(e)
    print('从数据库中获取')
    return resp_json, 200, {'Content-Type':'application/json'}
    

@api.route('/houses/info', methods = ['POST'])
@login_required
def save_house_info():
   """
      保存房屋的基本信息，前端发送过来的json数据
    {
        "title":"",
        "price":"",
        "area_id":"1",
        "address":"",
        "room_count":"",
        "acreage":"",
        "unit":"",
        "capacity":"",
        "beds":"",
        "deposit":"",
        "min_days":"",
        "max_days":"",
        "facility":["7","8"]
    }
   """ 
   user_id = g.user_id

   # 1.获取数据
   house_data = request.get_json()

   title = house_data.get("title")  # 房屋名称标题
   price = house_data.get("price")  # 房屋单价
   area_id = house_data.get("area_id")  # 房屋所属城区的编号
   address = house_data.get("address")  # 房屋地址
   room_count = house_data.get("room_count")  # 房屋包含的房间数目
   acreage = house_data.get("acreage")  # 房屋面积
   unit = house_data.get("unit")  # 房屋布局（几室几厅)
   capacity = house_data.get("capacity")  # 房屋容纳人数
   beds = house_data.get("beds")  # 房屋卧床数目
   deposit = house_data.get("deposit")  # 押金
   min_days = house_data.get("min_days")  # 最小入住天数
   max_days = house_data.get("max_days")  # 最大入住天数

    # 2.校验参数
   if not all([title, price, area_id, address, room_count, acreage, unit, capacity, beds, deposit, min_days, max_days]):
        return jsonify(errno=RET.PARAMERR, errmsg="参数不完整")

        #

    # 3.
   try:
       price = int( float(price)*100 )
       deposit = int( float(deposit)*100 )
   except Exception as e:
       current_app.logger.error(e)
       return jsonify(errno=RET.PARAMERR, errmsg = "参数错误")
   
   # 判断城区id是否存在
   try:
       area = Area.query.get(area_id)
   except Exception as e:
       current_app.logger.error(e)
       return jsonify(errno=RET.DBERR, errmsg = "数据库异常")

   if area is None:
       return jsonify(errno=RET.NODATA, errmsg = "城区信息有误")

   # 保存房屋信息
   house = House(
        user_id=user_id,
        area_id=area_id,
        title=title,
        price=price,
        address=address,
        room_count=room_count,
        acreage=acreage,
        unit=unit,
        capacity=capacity,
        beds=beds,
        deposit=deposit,
        min_days=min_days,
        max_days=max_days
   )

   # 处理房屋的设施信息
   facility_ids = house_data.get("facility")

   # 如果用户勾选了设施信息，再保存数据库
   if facility_ids:
       # ["7","8"]
       try:
           # select  * from ih_facility_info where id in []
           facilities = Facility.query.filter(Facility.id.in_(facility_ids)).all()
       except Exception as e:
           current_app.logger.error(e)
           return jsonify(errno=RET.DBERR, errmsg="数据库异常")   
       if facilities:
           # 表示有合法的设施数据
            # 保存设施数据( 表的多对多会自定关联和插上数据 )
            house.facilities = facilities

   try:
       db.session.add(house) # 只需要add(house) ， 不需要add( facilities )
       db.session.commit()  # 会修改两张表
   except Exception as e:
       current_app.logger.error(e)
       db.session.rollback()
       return jsonify(errno=RET.DBERR, errmsg="保存数据失败")

   return jsonify(errno = RET.OK, errmsg="OK", data={"house_id": house.id})



@api.route('/houses/image', methods = ["POST"])
@login_required
def save_houses_image():
   """
        保存房屋的图片
        参数：图片 和 房屋的id    
   """
   
   # 1.拿到一张上传的图片和房子的id
   image_file = request.files.get('house_image')
   house_id = request.form.get('house_id')

   if not all([image_file, house_id]):
       return jsonify(errno = RET.PARAMERR, errmsg="参数错误",)


   # 2.判断house的正确性
   try:
       house = House.query.get(house_id)
   except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="数据库异常") 

   if house is  None:
       return  jsonify(errno=RET.DBERR, errmsg="房屋不存在")

   image_data = image_file.read()
   file_name = image_file.filename 

   # 保存图片在服务器
   file_url =  './ihome/static/upload/'+str(house.id)+file_name
   try:
       with open(file_url, 'wb') as f:
            f.write(image_data)
   except Exception as e:
       return jsonify(errno =RET.IOERR, errmsg = "图片上传失败") 
  

   image_url = 'http://127.0.0.1:5000/static/upload/'+str(house.id)+file_name

   # 保存图片路径在数据库
   house_image = HouseImage(house_id = house_id, url = image_url)
   db.session.add(house_image)

   # 处理房屋的住图片,更新house对象
   if not house.index_image_url:
        house.index_image_url = image_url
        db.session.add(house)


   try:
        db.session.commit()  # 开始操作数据库
   except Exception as e:
       db.session.rollback()
       current_app.logger.error(e)
       return jsonify(errno =RET.DBERR, errmsg = "图片存储失败")

   return jsonify(errno =RET.OK, errmsg = "保存成功", data={'image_url':image_url}) 









