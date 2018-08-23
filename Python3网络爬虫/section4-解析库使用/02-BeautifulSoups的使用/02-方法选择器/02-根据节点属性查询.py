html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')

# 1.通过属性在查找节点
print(soup.find_all(attrs={'id': 'list-1'}))
print(soup.find_all(attrs={'name': 'elements'}))


print('############1###############')
# 2.简写
# 在这里我们直接传入 id='list-1' 就可以查询 id 为 list-1 的节点元素了。
# 而对于 class 来说，由于 class 在 python 里是一个关键字，
# 所以在这里后面需要加一个下划线，class_='element'，返回的结果依然还是 Tag 组成的列表
print(soup.find_all(id='list-1'))
print(soup.find_all(class_='element'))




