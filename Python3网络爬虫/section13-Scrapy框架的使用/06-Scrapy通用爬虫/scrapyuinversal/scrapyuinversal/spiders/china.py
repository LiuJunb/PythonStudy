# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapyuinversal.items import NewsItem
import re
from scrapyuinversal.itemloader import ChinaLoader

class ChinaSpider(CrawlSpider):
    name = 'china'
    allowed_domains = ['tech.china.com']
    start_urls = ['http://tech.china.com/articles']

    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )
    rules = (
        # 1。Spider 会在restrict_xpaths指定的区域查找所有的超链接并生成Requset。allow指定留下article开头的超链接
        # 2。指定callback函数是因为这些页面正是要解析为item的页面
        # 3.article/xxx.html 正则匹配： / 和 . 需要使用\转译
        Rule(
            LinkExtractor(allow='article\/.*\.html', restrict_xpaths='//div[@id="left_side"]//div[@class="con_item"]'),
            callback='parse_item'
        ),
        # callback 为空，这些页面不需要解析为item， follow 默认为 True (继续像上述情况一样分析)
        Rule(
            LinkExtractor(restrict_xpaths='//div[@id="pageStyle"]//a[contains(.,"下一页")]')
        )
    )

    def parse_item(self, response):
        loader = ChinaLoader(item=NewsItem(), response=response)
        loader.add_xpath('title', '//h1[@id="chan_newsTitle"]/text()')
        loader.add_value('url', response.url)
        loader.add_xpath('title', '//h1[@id="chan_newsTitle"]/text()')
        loader.add_xpath('text', '//div[@id="chan_newsDetail"]//text()')
        loader.add_xpath('datetime', '//div[@id="chan_newsInfo"]/text()', re='(\d+-\d+-\d+\s\d+:\d+:\d+)')
        loader.add_xpath('source', '//div[@id="chan_newsInfo"]/text()', re='来源：(.*)')
        loader.add_value('website', '中华网')
        yield loader.load_item()


    # 解析详情页面，例如：https://tech.china.com/article/20161209/201612098503.html
    # def parse_item(self, response):
    #     #i = {}
    #     #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
    #     #i['name'] = response.xpath('//div[@id="name"]').extract()
    #     #i['description'] = response.xpath('//div[@id="description"]').extract()
    #     #return i
    #
    #     item = NewsItem()
    #     item['title'] = response.xpath('//h1[@id="chan_newsTitle"]/text()').extract_first()
    #     item['url'] = response.url
    #     item['text'] = ''.join(response.xpath('//div[@id="chan_newsDetail"]//text()').extract()).strip()
    #     print(response.xpath('//div[@id="chan_newsInfo"]/text()').extract())
    #     item['datetime'] = response.xpath('//div[@id="chan_newsInfo"]/text()').re_first('(\d+-\d+-\d+\s\d+:\d+:\d+)')
    #     item['source'] = response.xpath('//div[@id="chan_newsInfo"]/text()').re_first('来源：(.*)').strip()
    #     item['website'] = '中华网'
    #     print('================================================')
    #     # print(item)
    #     # item['title'] = response.xpath('//h1[@id="chan_newsTitle"]/text()').extract_first()
    #     # item['url'] = response.url
    #     # item['text'] = ''.join(response.xpath('//div[@id="chan_newsDetail"]//text()').extract()).strip()
    #     # item['datetime'] = response.xpath('//div[@id="chan_newsInfo"]/text()').re_first('(\d+-\d+-\d+\s\d+:\d+:\d+)')
    #     # item['source'] = response.xpath('//div[@id="chan_newsInfo"]/text()').re_first('来源：(.*)').strip()
    #     # item['website'] = '中华网'
    #     return item




