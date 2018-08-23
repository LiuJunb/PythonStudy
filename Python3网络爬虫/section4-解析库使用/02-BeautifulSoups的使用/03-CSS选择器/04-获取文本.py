html = '''
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

# 先选中ul 在选中其中的li

for li in soup.select('li'):
    print(li['class'])
    # 下面两个功能一样
    print(li.string)
    print(li.get_text())
    print('============')
