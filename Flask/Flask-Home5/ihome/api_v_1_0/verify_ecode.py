# coding:utf-8

# 1.导入蓝图
from . import api
from flask import jsonify, current_app, make_response
# 导入response_code.py中的RET类
from ihome.utils.response_code import RET
# 导入captcha.py中的captcha类
from ihome.utils.captcha.captcha import captcha
# 2.导入ihome.__init__.py中的 redis_store
from ihome import redis_store



# http://127.0.0.1:5000/api/v1_0/image_codes/图片编号
@api.route('/image_codes/<image_code_id>', methods=['GET'])
def get_image_codes(image_code_id):
    """
        获取图片验证码
        :params image_code_id :图片验证码编号
        :return :成功返回 验证码图片； 失败 返回json字符串
    """
    # 1.获取参数
    # 2.验证参数
    if not image_code_id:
        return jsonify(error = RET.DBERR, errmsg = '参数为空')
    else:
    # 3.业务逻辑处理
        # 3.1生成验证码图片
        # 图片名称  文本  图片二进制码
        name, text, image_data = captcha.generate_captcha()

        # 3.2将验证码图片存在redis中,还要设计有效期
        # redis : 字符串  列表  哈希  set
        # 'image_codes':'xxxx'   字符串
        # 'image_codes':['', '', '']   列表
        # 'image_codes':{'编号1':'值1', '':'', '':''}   哈希。使用案例，hset('image_codes','编号1','值1') ；hget('image_codes','编号1')
        
        # 最后选择字符串类型，可以很好的设计有效期
        # 'image_codes_编号1'：'值1'
        # 'image_codes_编号2'：'值2'

        print(image_code_id)
        
        try:           
            image_codes_key = 'image_codes_%s' % image_code_id
            redis_store.set(image_codes_key, text)
            redis_store.expire(image_codes_key, 180)  # 这个key存在的时间是180s
            # 简写:              记录名称         有效期  文本
            # redis_store.setex(image_codes_key, 180, text)
        # except Exception , e:
        except Exception as e:
            # 记录日志
            current_app.logger.error(e)
            return jsonify(error = RET.DBERR, errmsg = '保存图片数据到redis失败')

        # 4.返回值
        # return image_data
        resp = make_response(image_data)
        resp.headers['Content-Type'] = 'image/jpg'
        return resp

   
