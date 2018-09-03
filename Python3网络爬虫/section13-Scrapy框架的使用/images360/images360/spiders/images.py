# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider, Request
from urllib.parse import urlencode
import json
from images360.items import ImageItem


class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['images.so.com']
    # start_urls = ['https://image.so.com/zj?ch=beauty&sn=0&listtype=new&temp=1']
    start_urls = ['https://image.so.com/zj?']

    # 这个是生成器函数
    def start_requests(self):
        data = {
            'ch': 'beauty',
            'listtype': 'new',
            'temp': '1'
        }
        base_url = 'https://image.so.com/zj?'
        for page in range(1, self.settings.get('MAX_PAGE') + 1):
            data['sn'] = page * 30
            params = urlencode(data)
            # print(params)
            url = base_url + params
            # 发起网络请求
            yield Request(url, self.parse)

    def parse(self, response):
        # 是一个json字符串
        # print(response.text)
        result = json.loads(response.text)
        for image in result.get('list'):
            item = ImageItem()
            item['id'] = image.get('imageid')
            item['url'] = image.get('qhimg_url')
            item['title'] = image.get('group_title')
            item['thumb'] = image.get('qhimg_thumb_url')
            yield item
