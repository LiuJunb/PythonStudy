# coding:utf-8
from werkzeug.routing import BaseConverter

# 1.自定义正则转换器
class ReConverter(BaseConverter):
    
    def __init__(self, url_map, regex):
        """调用父亲的初始化方法"""
        super(ReConverter, self).__init__(map)
        # 保存正则表达式
        self.regex = regex

