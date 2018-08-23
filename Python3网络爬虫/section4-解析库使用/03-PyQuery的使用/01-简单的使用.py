from pyquery import PyQuery as pq

# 1.解析网络上的一个网页
doc1 = pq(url='http://www.baidu.com')
# doc1 = pq(url='http://cuiqingcai.com')
print(doc1('title'))
print('=========1==========')

# 2.解析本地的网页：
doc2 = pq(filename='./test.html')
print(doc2)
print('=========2==========')

# 3.解析字符串
html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
doc3 = pq(html)
print(doc3('li'))