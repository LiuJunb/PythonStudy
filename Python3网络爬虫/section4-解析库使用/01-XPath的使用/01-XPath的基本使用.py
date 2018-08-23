from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
# XPath 解析对象
html = etree.HTML(text)
print(html)  # <Element html at 0x1051fc648>

# 查看修正后的 HTML 代码。
# decode() 将bytes转成字符窜, 解码
# encode() 将字符窜转成bytes, 编码

result = etree.tostring(html)
print(result.decode('utf-8'))




