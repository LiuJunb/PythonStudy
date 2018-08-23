import re

html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君"><i class="fa fa-user"></i>但愿人长久</a>
        </li>
    </ul>
</div>'''

# 1.获取所有 a 节点的超链接、歌手和歌名
results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
# print(result)
print(type(results))  # <class 'list'>

for result in results:
    print(result)
    # print(type(value))  # <class 'tuple'>


print('===================')
# 获取所有 a 节点的超链接、歌手和歌名: (?:<i.*?></i>)?
# ()? 代表这个组可有可无，0 或者 1 个
# ?:代表是否要将结果放到一个分组里面去
results2 = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(?:<i.*?></i>)?(.*?)</a>', html, re.S)
for result in results2:
    print(result)

print('===================')
results3 = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(<i.*?></i>)?(.*?)</a>', html, re.S)

# print(results3.group(1))  # 使用findall不能使用group函数
for result in results3:
    print(result)  # 有四个分组
    # print(result[0], result[1], result[2], result[3])