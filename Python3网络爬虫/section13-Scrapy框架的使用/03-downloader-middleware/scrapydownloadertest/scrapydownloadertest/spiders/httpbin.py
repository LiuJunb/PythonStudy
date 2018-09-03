# -*- coding: utf-8 -*-
import scrapy


class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/get']
    # allowed_domains = ['www.baidu.com']
    # start_urls = ['http://www.baidu.com']

    def parse(self, response):
        print('=========================')
        print(response.status)
        self.logger.debug(response.text)  # 这个打印是异步的
        print('=========================')
