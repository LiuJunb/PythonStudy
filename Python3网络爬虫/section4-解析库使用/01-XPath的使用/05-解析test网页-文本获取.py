from lxml import etree

# 构建xpath对象
html = etree.parse('./test.html', etree.HTMLParser())
result = etree.tostring(html)
# print(result.decode('utf8'))


#  1.获取li节点存在class="item-0"里面的文本
result1 = html.xpath('//li[@class="item-0"]/text()')
print(result1)  # ['\n     ']

# 2.获取li节点存在class="item-0"里面a节点的文本
result2 = html.xpath('//li[@class="item-0"]/a/text()')
print(result2)  # ['first item', 'fifth item']

# 3.获取li节点存在class="item-0"里面a节点的文本
# 选取所有子孙节点的文本
result3 = html.xpath('//li[@class="item-0"]//text()')
print(result3)  # ['first item', 'fifth item', '\n     ']




















