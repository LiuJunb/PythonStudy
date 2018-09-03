import requests
from urllib.parse import urlencode
import os
from hashlib import md5

headers = {
    'Host': 'www.toutiao.com',
    'Referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/69.0.3489.1 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}


# 1.下载网页
def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
    }
    # 将字典转成url参数
    print(urlencode(params))  # offset=0&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&cur_tab=1
    url = 'http://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        print('ConnectionError')
        return None


def get_images(json):

    if json['data']:
        datas = json.get('data')
        # print(datas)
        for item in datas:
            # 判读一个key是否存在字典中
            if 'cell_type' in item:
                pass
                # print('cell_type')
            else:
                title = item.get('title')
                image_list = item.get('image_list')
                # print(title)
                # print(image_list)
                for image in image_list:
                    yield {
                        'image': image.get('url'),
                        'title': title
                    }


# https://p3.pstatp.com/list/pgc-image/1534995396249a8a73c285e
# {'image': '//p1.pstatp.com/list/pgc-image/15349953971644cc69e1c9c', 'title': '成都街拍，有一种时尚，叫简单的美！'}
def save_image(item):
    # 1.如果文件夹不存在,就新建一个文件夹
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        # 获取图片不需要添加头
        response = requests.get('https:'+item.get('image'))
        if response.status_code == 200:
            # 2.图片的名称
            file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
            # 3.如果图片还不存在就把图片写到文件中
            if not os.path.exists(file_path):
                # 4.开始写文件
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image')


if __name__ == '__main__':
    json = get_page(0)
    # 拿到一个字典数组
    results = get_images(json)
    for result in results:
        save_image(result)
