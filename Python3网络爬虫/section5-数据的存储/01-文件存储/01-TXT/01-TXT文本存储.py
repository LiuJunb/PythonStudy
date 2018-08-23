import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/69.0.3489.1 Safari/537.36'
}
# 1.拿到了字符串
html = requests.get(url, headers=headers).text

# 2.将字符串构建成pyquery对象
doc = pq(html)

# 3.查找对应的节点
items = doc('.explore-tab .feed-item').items()


print('='*30)  # ==============================

# 4.遍历迭代器函数
for item in items:
    question = item.find('h2').text()
    author = item.find('.author-link-line').text()
    answer = pq(item.find('.content').html()).text()
    # 5.打开文件： 追加
    file = open('explore.txt', 'a', encoding='utf-8')
    # 6.写文件
    file.write('\n'.join([question, author, answer]))
    file.write('\n' + '=' * 50 + '\n')  # 分割线
    # 7.关闭文件
    file.close()