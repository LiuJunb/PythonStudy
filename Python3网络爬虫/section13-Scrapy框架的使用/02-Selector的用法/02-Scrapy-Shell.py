# xpath
# 1.选中多个a节点
# result = response.selector.xpath('//a')

# 2.提取a节点 :
# result.extract()

# 3.提取第一个节点
# result.extract_first()

# 3.提取第一个节点(设置默认值)
# result.extract_first('Default Value')

# 4.提取节点的文本
# response.xpath('//a/text()')
# response.xpath('//a/text()').extract()
# response.xpath('//a[@href="image1.html"]/text()').extract()

# 5.提取属性
# response.xpath('//a/@href').extract_first()


# =====================================================


# css

# 1.选中a节点
# result = response.css('a[href="image1.html"] img')

# 2.提取多个img节点 : ['<img src="image1_thumb.jpg">']
# response.css('a[href="image1.html"] img').extract()

# 3.提取第一个节点 : ['<img src="image1_thumb.jpg">']
# response.css('a[href="image1.html"] img').extract()[0]
# response.css('a[href="image1.html"] img').extract_first()

# 4.提取节点的文本 : ['Name: My image 1 ']
# response.css('a[href="image1.html"]::text').extract()

# 5.提取属性 : ['image1_thumb.jpg']
# response.css('a[href="image1.html"] img::attr(src)').extract()



# =====================================================


# 正则匹配
# 1.获取a标签的文本
# response.xpath('//a/text()')

# [<Selector xpath='//a/text()' data='Name: My image 1 '>, <Selector xpath='//a/text()' data='Name: My image 2 '>, <Selector xpath='//a/text()' data='Name: My image 3 '>, <Selector xpath='//a/text()' data='Name: My image 4 '>, <Selector xpath='//a/text()' data='Name: My image 5 '>]

# 2.提取a标签中的文本
# response.xpath('//a/text()').re('Name:\s(.*)')
# 结果是分组中的内容：['My image 1 ', 'My image 2 ', 'My image 3 ', 'My image 4 ', 'My image 5 ']

# 3.提取其中的第一个文本
# response.xpath('//a/text()').re_first('Name:\s(.*)')
# 结果是分组中的内容： 'My image 1 '