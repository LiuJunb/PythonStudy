# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class ImageItem(Item):
    # 定义类属性
    collection = table = 'images'  # 代表是表名
    id = Field()   # 代表是字段
    url = Field()
    title = Field()
    thumb = Field()


class Images360Item(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
