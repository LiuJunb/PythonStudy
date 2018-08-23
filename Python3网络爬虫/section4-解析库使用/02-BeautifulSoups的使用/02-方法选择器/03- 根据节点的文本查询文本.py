import re
html='''
<div class="panel">
    <div class="panel-body">
        <a>Hello, this is a link</a>
        <a>Hello, this is a link, too</a>
        <a>link</a>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')

# 调用 find_all() 方法传入 text 参数，参数为正则表达式对象，结果会返回所有匹配正则表达式的节点文本组成的列表
# 1.查找节点文本中包含link字符的所有节点对应的文本
print(soup.find_all(text=re.compile('link')))  # 返回的是文本数列

# 2.精准的查找文本
print(soup.find_all(text='link'))


# 3.find_parent()
print(soup.find_parent(name='a'))
print(soup.find_parent(attrs={'class': 'panel-body'}))
