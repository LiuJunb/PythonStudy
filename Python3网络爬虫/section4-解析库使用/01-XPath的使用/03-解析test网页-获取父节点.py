from lxml import etree

# 构建xpath对象
html = etree.parse('./test.html', etree.HTMLParser())
result = etree.tostring(html)
# print(result.decode('utf8'))


#  1.获取a节点的父亲节点的class
result1 = html.xpath('//a[@href="link4.html"]')  # [<Element a at 0x1046e5788>]
result2 = html.xpath('//a[@href="link4.html"]/../a[@class]')  # [<Element a at 0x101074708>] 取到父亲的的直接儿子
result3 = html.xpath('//a[@href="link4.html"]/..')  # [<Element li at 0x109b9e788>] 取到父亲
result4 = html.xpath('//a[@href="link4.html"]/../@class')  # ['item-1']  取到父亲的class
print(result1, result2, result3, result4, sep='\n')

# 2.通过parent::*来获取父亲的节点
result5 = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result5)  # ['item-1']









