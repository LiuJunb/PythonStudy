# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapyuinversal.utils import get_config
from scrapyuinversal.rules import rules
from scrapyuinversal.items import NewsItem
from scrapyuinversal.itemloader import ChinaLoader
from scrapyuinversal import urls


class UniversalSpider(CrawlSpider):
    name = 'universal'

    def __init__(self, name, *args, **kwargs):
        config = get_config(name)
        self.config = config

        start_urls = config.get('start_urls')
        if start_urls:
            if start_urls.get('type') == 'static':
                self.start_urls = start_urls.get('value')
            elif start_urls.get('type') == 'dynamic':
                self.start_urls = list(eval('urls.' + start_urls.get('method'))(*start_urls.get('args', [])))

        self.rules = rules.get(config.get('rules'))
        # self.start_urls = config.get('start_urls')
        self.allowed_domains = config.get('allowed_domains')
        # super(UniversalSpider, self).__init__(*args, **kwargs)
        # or
        super().__init__(*args, **kwargs)

    def parse_item(self, response):
        item = self.config.get('item')
        if item:
            cls = eval(item.get('class'))()
            loader = eval(item.get('loader'))(cls, response=response)
            # 动态获取属性配置
            for key, value in item.get('attrs').items():
                for extractor in value:
                    if extractor.get('method') == 'xpath':
                        loader.add_xpath(key, *extractor.get('args'), **{'re': extractor.get('re')})
                    if extractor.get('method') == 'value':
                        loader.add_value(key, *extractor.get('args'), **{'re': extractor.get('re')})
                    if extractor.get('method') == 'css':
                        loader.add_css(key, *extractor.get('args'), **{'re': extractor.get('re')})
                    if extractor.get('method') == 'attr':
                        # getattr()  ==> response.url
                        loader.add_value(key, getattr(response, *extractor.get('args')))
            yield loader.load_item()