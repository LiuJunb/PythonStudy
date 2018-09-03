from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote

from pyquery import PyQuery as pq

import pymongo

MONGO_URL = 'localhost'
PORT = 27017
MONGO_DB = 'taobao'
MONGO_COLLECTION = 'products'
client = pymongo.MongoClient(host=MONGO_URL, port=PORT)
db = client[MONGO_DB]

browser = webdriver.Chrome()

# 显示等待时间10秒
wait = WebDriverWait(browser, 10)
KEYWORD = 'iPad'


def index_page(page):
    """
      抓取索引页 1
      :param page: 页码
    """
    print('正在爬取第', page, '页')
    try:
        # 1。quote 对 url 编码
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        # 2。发起网络请求
        browser.get(url)
        if page > 1:
            # 3。显示等待 想要的标签加载完毕
            # 页码输入框
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
            # 确认跳转到指定的页码
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
            # 清楚页码输入框
            input.clear()
            # 手动设置页码
            input.send_keys(page)
            # 点击获取对用页码的数据( 相当于再发起一个网络请求 )
            submit.click()

        # 等待当前是 第 几个 页码加载完毕
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
        # 拿到每一个商品 item
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))

        get_products()

    # 超时后从新爬取
    except TimeoutException:
        index_page(page)


def get_products():
    """
    提取商品数据
    """
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)


def save_to_mongo(result):
    """
    保存至MongoDB
    :param result: 结果
    """
    try:
        if db[MONGO_COLLECTION].insert(result):
            print('存储到MongoDB成功')
    except Exception:
        print('存储到MongoDB失败')


MAX_PAGE = 100


def main():
    """
    遍历每一页
    """
    for i in range(1, MAX_PAGE + 1):
        index_page(i)


if __name__ == '__main__':
    main()






