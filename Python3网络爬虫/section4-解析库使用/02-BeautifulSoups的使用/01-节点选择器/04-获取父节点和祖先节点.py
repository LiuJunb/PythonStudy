html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
        </p>
        <p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')

# 1.获取直接父亲节点
print(soup.a.parent)  # p 节点


print('*******************************')

html2 = """
<html>
    <body>
        <p class="story">
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
        </p>
"""
soup2 = BeautifulSoup(html2, 'lxml')
print(type(soup2.a.parents))  # <class 'generator'>
# print(list(enumerate(soup2.a.parents)))
for i, child in enumerate(soup2.a.parents):
    print(i, child)




