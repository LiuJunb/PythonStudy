# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class TutorialPipeline(object):
#     def process_item(self, item, spider):
#         return item

from scrapy.exceptions import DropItem
import pymongo


# 1.这个是用来处理数据的 Item Pipeline
class TextPipeline(object):
    def __init__(self):
        self.limit = 50

    def process_item(self, item, spider):
        if item['text']:
            if len(item['text']) > self.limit:
                item['text'] = item['text'][0:self.limit].rstrip() + '...'
            return item
        else:
            return DropItem('Missing Text')


# 2.这个是用来保存数据到本地 Pipeline  3.到setting.py中配置使用
class MongoPineline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    # 类方法（ 是通过依赖注入的方式 ）
    @classmethod
    def from_crawler(cls, crawler):
        # 通过 crawler 可以拿到全局配置setting.py
        return cls(
          mongo_uri=crawler.settings.get('MONGO_URI'),
          mongo_db=crawler.settings.get('MONGO_DB')
        )

    # 打开数据库
    def open_spider(self, spider):
        # 如果不指定ip  和 端口 默认使用localhost 和 27017
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    # 这个是存储数据的回调
    def process_item(self, item, spider):
        # 获取class的名称作为collection的名称
        name = item.__class__.__name__
        self.db[name].insert(dict(item))
        return item

    # 关闭数据库
    def close_spider(self, spider):
        self.client.close()


