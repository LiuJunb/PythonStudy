# 爬虫的目标：提取出猫眼电影 TOP100 榜的电影名称、时间、评分、图片等信息
import requests
import re
import json
import time
from requests.exceptions import RequestException

headers = {

    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/69.0.3489.1 Safari/537.36'
}


def get_one_page(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text


def write_to_json(content):
    """"""
    with open('result.txt', 'a') as f:
        # 第一种
        # json.dump(content, f, ensure_ascii=False)   # <class 'NoneType'>

        # 第二种： ensure_ascii=False 支持中文
        print(type(json.dumps(content, ensure_ascii=False).encode('utf-8')))  # <class 'bytes'>
        print(type(json.dumps(content, ensure_ascii=False)))  # <class 'str'>
        f.write(json.dumps(content, ensure_ascii=False))  # 参数是 str 因为打开文件的格式是 a 而不是wb
        f.write('\n')


def parse_one_page(html):
    """生产器函数"""
    # results = re.findall('<dd>.*?board-index.*?>(.*?)</i>'  # 1.取电影排名信息
    #                      '.*?data-src="(.*?)".*?'  # 2.取出电影图片
    #                      'class="name">.*?>(.*?)</a>'  # 3.取出调用名称
    #                      '.*?class="star">\s+(.*?)</p>'  # 4.主演, 上映时间
    #                      '.*?class="releasetime">(.*?)</p>'  # 5.上映时间
    #                      '.*?class="integer">(.*?)</i>'  # 6.评分
    #                      '.*?class="fraction">(.*?)</i>', html, re.S)  # 7.评分

    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>'  # 1.取电影排名信息
                         '.*?data-src="(.*?)".*?'  # 2.取出电影图片
                         'class="name">.*?>(.*?)</a>'  # 3.取出调用名称
                         '.*?class="star">\s+(.*?)</p>'  # 4.主演, 上映时间
                         '.*?class="releasetime">(.*?)</p>'  # 5.上映时间
                         '.*?class="integer">(.*?)</i>'  # 6.评分
                         '.*?class="fraction">(.*?)</i>', re.S)
    items = re.findall(pattern, html)

    # 遍历元组
    for item in items:
        # print(item[3].strip())  # 主演：张国荣,张丰毅,巩俐
        # print(item[3].strip()[3:])  # 张国荣,张丰毅,巩俐
        # print('liujun'[3:])  # jun

        # print(item[4].strip()) # 上映时间：1993-01-01(中国香港)
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2].strip(),
            'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
            'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
            'score': item[5].strip() + item[6].strip()
        }


def main(offset):
    url = 'http://maoyan.com/board/'+str(offset)
    html = get_one_page(url)
    # 遍历生产器函数
    for item in parse_one_page(html):
        # print(item)
        # 写到文件
        write_to_json(item)


# 入口函数
if __name__ == '__main__':
    print(range(10))  # range(0, 10)

    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)




