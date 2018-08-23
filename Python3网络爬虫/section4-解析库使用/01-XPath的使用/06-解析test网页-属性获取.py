from lxml import etree

# 构建xpath对象
html = etree.parse('./test.html', etree.HTMLParser())
result = etree.tostring(html)
# print(result.decode('utf8'))


#  1.获取li节点里面a节点的href
result1 = html.xpath('//li/a/@href')
print(result1)  # ['link1.html', 'link2.html', 'link3.html', 'link4.html', 'link5.html']

# 2.属性多值匹配（ 失败 ）
text = '''
<li class="li li-first"  name="item"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result2 = html.xpath('//li[@class="li"]/a/text()')
print(result2)  # []


# 3.属性多值匹配 （成功）
result3 = html.xpath('//li[contains(@class, "li")]/a/text()')
print(result3)  # ['first item']


# 4.多属性匹配
result4 = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print(result4)

# 5.按序选择
result5 = html.xpath('//li[1]/a/text()')
print(result5)















