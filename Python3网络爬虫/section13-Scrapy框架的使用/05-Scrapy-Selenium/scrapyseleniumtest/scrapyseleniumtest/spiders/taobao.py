# -*- coding: utf-8 -*-
from scrapy import Request, Spider
from urllib.parse import quote
from scrapyseleniumtest.items import ProductItem


class TaobaoSpider(Spider):
    name = 'taobao'
    allowed_domains = ['www.taobao.com']
    start_urls = ['https://s.taobao.com/search?q=']
    base_url = 'https://s.taobao.com/search?q='

    def start_requests(self):
        for keyword in self.settings.get('KEYWORDS'):
            for page in range(1, self.settings.get('MAX_PAGE') + 1):
                url = self.base_url + quote(keyword)
                print('==================1.start_requests================')
                print(url)
                # meta={'page': page} 传递参数
                # dont_filter=True  不去重复
                yield Request(url=url, callback=self.parse, meta={'page': page}, dont_filter=True)

    # 这里面拿到的是一个网页
    # https://s.taobao.com/search?q=iPad$xxxxx
    def parse(self, response):
        print('##############3.###################')
        # print(response.text)
        products = response.xpath(
            '//div[@id="mainsrp-itemlist"]//div[@class="items"][1]//div[contains(@class,"item")]'
        )
        for product in products:
            item = ProductItem()
            item['price'] = ''.join(product.xpath('.//div[contains(@class,"price")]//text()').extract()).strip()
            item['title'] = ''.join(product.xpath('.//div[contains(@class,"title")]//text()').extract()).strip()
            item['shop'] = ''.join(product.xpath('.//div[contains(@class,"shop")]//text()').extract()).strip()
            item['image'] = ''.join(product.xpath('.//div[@class="pic"]/a/img/@data-src').extract()).strip()

        print(item)
        yield item


