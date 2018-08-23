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
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')

# 关联选择
# print(soup.p)  # 选中第一个p

# 1.children 返回的是生成器类型(直接子节点的列表)
print(soup.p.children)  # <list_iterator object at 0x1047c64a8>

for i, child in enumerate(soup.p.children):
    print(i, child)

print('========================')
# 2.得到所有的子孙节点(列表)
print(soup.p.descendants)
for i, child in enumerate(soup.p.descendants):
    print(i, child)


print('************************')
# 3.父节点和祖先节点


