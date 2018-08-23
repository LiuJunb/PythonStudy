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


print(soup.select('.panel .panel-heading'))  # 返回一个数列

print('======================')
print(soup.select('ul li'))  # 返回一个数列


print(soup.select('#list-2 .element'))  # 返回一个数列
print(type(soup.select('ul')[0]))  # <class 'bs4.element.Tag'>