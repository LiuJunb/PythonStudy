# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import QuoteItem
"""
    <div itemtype=”http://schema.org/CreativeWork">
    
        <span class="text” itemprop=”text”>“The world as we have created it is a process        thinking. It cannot
                be changed without changing our thinking.”</span>
        
        <span>by <small class="author” itemprop=”author”>Albert Einstein</small> 
            <a href=”/author/Albert-Einstein”>(about)</a>
        </span>
        
        <div class=”tags”>
            Tags :
            <meta class="keywords” itemprop=”keywords” content=”change,deep-thoughts,thinking,world”> 
            <a class=”tag” href=”/tag/change/page/1/”>change</a>
            <a class=”tag” href=”/tag/deep-thoughts/page/1/”>deep-thoughts<la>
            <a class=”tag” href=”/tag/thinking/page/1/”>thinking<la>
            <a class=”tag” href="/tag/world/page/1/”>world</a>
        </div>
    </div>
"""


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']
    # allowed_domains = ['travel.qunar.com']
    # start_urls = ['http://travel.qunar.com/travelbook/list.htm?order=hot_heat']

    def parse(self, response):

        # pass
        quotes = response.css('.quote')
        # quotes = response.css('li > .tit > a')
        print('#####################')
        print(response)  # 打印 <200 http://quotes.toscrape.com/>
        print('#####################')
        for quote in quotes:
            # ::text 获取正文
            item = QuoteItem()
            print('========================')
            # print(quote.css('.tags .tag::text').extract())
            item['text'] = quote.css('.text::text').extract_first()  # 拿到列表中的第一个元素
            item['author'] = quote.css('.author::text').extract_first()
            item['tags'] = quote.css('.tags .tag::text').extract()  # 获取整个列表
            print(quote.css('.tags .tag::text'))
            yield item
        # 拿到的值 ： /page/2/
        next = response.css('.pager .next a::attr(href)').extract_first()
        # 拿到的值：http://quotes.toscrape.com/page/2/
        url = response.urljoin(next)
        print(next, url)
        yield scrapy.Request(url=url, callback=self.detail_parse)

    def detail_parse(self, response):
        self.parse(response)


# 编写完成整个爬虫（蜘蛛）后怎么执行？
# 在命令行执行：scrapy crawl quotes
# 在命令行执行：scrapy crawl quotes -o quotes.json  将爬出的结果输出的一个json文件(追加)
# 在命令行执行：scrapy crawl quotes -o quotes.csv
# 在命令行执行：scrapy crawl quotes -o quotes.xml
# 在命令行执行：scrapy crawl quotes -o quotes.pickle
# 如果想要输出到数据库可以使用：Item Pileline 来完成






