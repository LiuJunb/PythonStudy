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
items = doc('.list')

li = doc('.item-0.active')
print(li)
print(type(li))
print(str(li))

print('===================')
lis = doc('li')
print(type(lis))  # <class 'pyquery.pyquery.PyQuery'>
print(lis)

print('#####################')
# 1.使用.items来遍历
lis = doc('li').items()
print(type(lis))  # <class 'generator'>
for li in lis:  # 遍历生成器函数
    print(li, type(li))   # <class 'pyquery.pyquery.PyQuery'>
