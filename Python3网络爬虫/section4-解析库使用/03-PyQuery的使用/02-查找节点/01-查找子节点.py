html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
from pyquery import PyQuery as pq
doc = pq(html)

items = doc('.list')
print(type(items))  # <class 'pyquery.pyquery.PyQuery'>
print(items)

print('=======1=======')
# 1.使用find(self, selector):来查找节点
lis = items.find('li')  # 查找出所有的li
print(type(lis))  # <class 'pyquery.pyquery.PyQuery'>
print(lis)

print('=======2=======')
# 2.使用children(self, selector=None):来查找child
lis = items.children()
print(type(lis))  # <class 'pyquery.pyquery.PyQuery'>
print(lis)

print('=======3=======')
# 3.使用children(self, selector=None):来查找child
lis = items.children('.active')
print(type(lis))  # <class 'pyquery.pyquery.PyQuery'>
print(lis)
