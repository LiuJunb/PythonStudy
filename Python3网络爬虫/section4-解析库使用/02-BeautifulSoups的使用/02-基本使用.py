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

#  prettify() 方法，这个方法可以把要解析的字符串以标准的缩进格式输出，在这里注意到输出结果里面包含了 body 和 html 节点，
# 也就是说对于不标准的 HTML 字符串 BeautifulSoup 可以自动更正格式
print(soup.prettify())

#  soup.title 就可以选择出 HTML 中的 title 节点
print(soup.title.string)  # The Dormouse's story

