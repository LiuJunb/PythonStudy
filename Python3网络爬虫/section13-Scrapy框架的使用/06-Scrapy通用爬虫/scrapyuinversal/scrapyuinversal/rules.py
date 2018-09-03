from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

rules = {
    'china': (
        Rule(
            LinkExtractor(allow='article\/.*\.html', restrict_xpaths='//div[@id="left_side"]//div[@class="con_item"]'),
            callback='parse_item'
        ),
        # callback 为空，这些页面不需要解析为item， follow 默认为 True (继续像上述情况一样分析)
        Rule(
            LinkExtractor(restrict_xpaths='//div[@id="pageStyle"]//a[contains(.,"下一页")]')
        )
    )
}

