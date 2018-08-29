from scrapy import Selector

body = '<html><head><title>Hello world</title></head></html>'
# 这个代码可以下载parse函数中
selector = Selector(text=body)
# title = selector.xpath('//title/text()').extract_first()
# or
title = selector.css('title::text').extract()
print(title)