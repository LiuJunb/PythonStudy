html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
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

# 1.通过节点选择器找到第一个li
print(soup.li)   # <li class="element">Foo</li>

print('###############1#############')
# 2.通过方法find_all，根据节点名找节点
# find_all(name , attrs , recursive , text , **kwargs)
print(soup.find_all(name='ul'))  # 是一个数列, 数列存的是节点对象
print(type(soup.find_all(name='ul')[0]))  # class 'bs4.element.Tag'>


print('#############2###############')
# 3.遍历ul中所有的li
for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
    for li in ul.find_all(name='li'):
        print(li.string)


print('#############3###############')
# 4.find_parent( 指定查找的parent )
print(soup.find(name='li').find_parent(name='ul'))
print('-------')
print(soup.find(name='ul').find_parent(attrs={'class': 'panel'}))

