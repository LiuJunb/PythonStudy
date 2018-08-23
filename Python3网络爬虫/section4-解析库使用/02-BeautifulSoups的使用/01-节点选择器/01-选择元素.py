html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')

print(soup.title)  # <title>The Dormouse's story</title>
print(type(soup.title))  # <class 'bs4.element.Tag'>

print(soup.title.string)  # The Dormouse's story
print(soup.head)  # <head><title>The Dormouse's story</title></head>
print(soup.p)  # <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
print('---------------')
#print(soup.body)

print('===============')
# 1.获取节点的名称
print(soup.title.name)  # title

# 2.获取节点的属性
print(soup.p.attrs)  # {'class': ['title'], 'name': 'dromouse'}
print(soup.p.attrs['name'])  # dromouse

# 3.获取节点的内容
print(soup.p.string)  # The Dormouse's story

# 4.




