html = """
<html><head><title>The Dormouse's story</title></head>
<body>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')

print(soup.title)  # <title>The Dormouse's story</title>

# 嵌套选择
print(soup.head.title)  # <title>The Dormouse's story</title>

print(type(soup.head.title))  # <class 'bs4.element.Tag'>
print(soup.head.title.string)  # The Dormouse's story


