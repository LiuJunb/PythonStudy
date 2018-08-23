html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active">哈哈<a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
from pyquery import PyQuery as pq
doc = pq(html)


# 1.获取文本
a = doc('.item-0.active a')
print(a)
print(a.text())  # third item

print('################')
# 2.获取这个节点内部的 HTML 文本
li = doc('.item-0.active')
print(li)
print(li.html())

print('@@@@@@@@@@@@@@@@@@@')
# 3. 获取多个li标签中的文本
li = doc('li')
print(li.html())  # 默认第一个
# text() 则返回了所有的 li 节点内部纯文本
print(li.text())  # 所有li里面所有的文本
print(type(li.text()))  # <class 'str'>

