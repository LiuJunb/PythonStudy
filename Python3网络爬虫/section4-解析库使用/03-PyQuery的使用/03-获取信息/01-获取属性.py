html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
from pyquery import PyQuery as pq
doc = pq(html)

a = doc('.item-0.active a')
print(a, type(a))
# 1.获取属性：attr(self, *args, **kwargs)
print(a.attr('href'))  # link3.html
print(a.attr.href)  # link3.html
print('========2==========')
# 2.选中多个a标签获取属性 （ 只获取第一个标签的属性 ）
a = doc('a')
print(a, type(a))
print(a.attr('href'))  # link2.html
print(a.attr.href)  # link2.html

print('========3==========')
# 3.遍历多个a标签，获取属性
a = doc('a')
for item in a.items():
    print(item.attr('href'))

