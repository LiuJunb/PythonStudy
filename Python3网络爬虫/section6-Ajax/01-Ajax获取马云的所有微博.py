from urllib.parse import urlencode
import requests
from pyquery import  PyQuery as pq
from pymongo import MongoClient

client = MongoClient(host='localhost', port=27017)
db = client['weibo']   # 数据库
collection = db['weibo']  # collection

base_url = 'https://m.weibo.cn/api/container/getIndex?'

# Host 用于指定请求资源的主机 IP 和端口号，其内容为请求 URL 的原始服务器或网关的位置
# Referer 此内容用来标识这个请求是从哪个页面发过来的，服务器可以拿到这一信息并做相应的处理，如做来源统计、做防盗链处理等
headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2145291155',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/69.0.3489.1 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}


def get_page(pageIndex):
    params = {
        'type': 'uid',
        'value': '2145291155',
        'containerid': '1076032145291155',
        'page': pageIndex
    }

    url = base_url + urlencode(params)

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()

    except requests.ConnectionError as e:
        print('Error', e.args)


def parse_page(json):
    print('parse_page')
    if json:
        # 1.拿到多篇微博
        # items = json.get('cards')
        items = json['data'].get('cards')
        # 2.遍历微博
        for item in items:
            item = item['mblog']
            weibo = {}
            weibo['id'] = item.get('id')
            weibo['text'] = pq(item.get('text')).text()
            print(weibo['text'])
            weibo['attitudes'] = item.get('attitudes_count')
            weibo['comments'] = item.get('comments_count')
            weibo['reposts'] = item.get('reposts_count')

            yield weibo


def save_to_mongo(result):
    if collection.insert(result):
        print('Save to Mongodb')


if __name__ == '__main__':
    # 1.发起ajax
    json = get_page(0)
    print(type(json))  # <class 'dict'>
    # 2.解析json
    results = parse_page(json)
    # 3.遍历生成器函数( 如果不遍历生成器函数，那么生成器函数没有执行 )
    for result in results:
        # print(result)
        save_to_mongo(result)




