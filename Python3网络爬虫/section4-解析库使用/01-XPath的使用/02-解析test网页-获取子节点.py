from lxml import etree


html = etree.parse('./test.html', etree.HTMLParser())
result1 = etree.tostring(html)
# print(result1.decode('utf-8'))


# 1.找到-所有节点
result2 = html.xpath('//*')
# print(result2)  # [<Element html at 0x10e2cd708>, <Element body at 0x10e2cd6c8>,.. ]

# 2.获取所有 li 节点
result3 = html.xpath('//li')
# print(result3)  # [<Element li at 0x1020cf788>, <Element li at 0x1020cf848>, ..]
# print(result3[0])

# 3.查找元素的子节点或子孙节点(选择 li 节点所有直接 a 子节点)
result4 = html.xpath('//li/a')
# print(result4)  # [<Element a at 0x103577808>, <Element a at 0x103577888>,..]

# 4.获取 ul 节点下的所有子孙 a 节点
result5 = html.xpath('//li//a')
# print(result5)  # [<Element a at 0x103577808>, <Element a at 0x103577888>,..]

# 5.获取ul节点下直接的 a 节点
result6 = html.xpath('//ul/a')
print(result6)  # []


