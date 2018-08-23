html = '''
<ul class="list">
     <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
</ul>
'''
from pyquery import PyQuery as pq
doc = pq(html)


li = doc('.item-0.active')
print(li)
print('======================')
li.attr('name', 'link')  # 添加一个属性
print(li)
print('----------------------')
li.text('changed item')  # 覆盖里面的内容为字符串
print(li)
print('########################')
li.html('<span>changed item</span>') # 覆盖里面的内容为html
print(li)



