html = """
<html>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">Bob</a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
        </p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')

print('Next Sibling:')
print(type(soup.a.next_sibling))  # <class 'bs4.element.Tag'>
print(soup.a.next_sibling)  # <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
# 2.获取标签的值
print(soup.a.next_sibling.string)  # Lacie

print('*************************')
print('Parent:')
print(type(soup.a.parents))
print(list(soup.a.parents)[0])  # p
# 1.获取标签的属性
print(list(soup.a.parents)[0].attrs['class'])  #  ['story']