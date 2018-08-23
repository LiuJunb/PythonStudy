from lxml import etree

# 构建xpath对象
html = etree.parse('./test.html', etree.HTMLParser())
result = etree.tostring(html)
# print(result.decode('utf8'))


#  1.获取li节点存在class="item-0"
result1 = html.xpath('//li[@class="item-0"]')
print(result1)  # [<Element li at 0x10d1ab608>, <Element li at 0x10d1ab648>]

#














