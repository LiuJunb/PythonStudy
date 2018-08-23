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

# 1.使用parent(self, selector=None)来获取父亲节点
container = items.parent()
print(type(container))  # <class 'pyquery.pyquery.PyQuery'>
print(container)  # <div id="container">


print('-======================')
# 2.使用parents(self, selector=None):来获取祖先节点
parents = items.parents()
print(type(parents))
# 在这里我们调用了 parents() 方法，可以看到输出结果有两个，
# 一个是 class 为 wrap 的节点，一个是 id 为 container 的节点，
# 也就是说，parents() 方法会返回所有的祖先节点
print(parents())

print('########################')
# 3.使用parents(self, selector=None):来获取祖先节点
parent = items.parents('.wrap')
print(parent)

