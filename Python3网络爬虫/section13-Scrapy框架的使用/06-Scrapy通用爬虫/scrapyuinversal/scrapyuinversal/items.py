# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class NewsItem(Item):
    collection = table = 'news'  # 表的名称
    title = Field()  # 标题
    url = Field()   # 链接
    text = Field()  # 正文
    datetime = Field()  # 发布时间
    source = Field()    # 来源
    website = Field()   # 站点名称