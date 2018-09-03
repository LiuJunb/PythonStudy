from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
import requests
from pyquery import PyQuery as pq

import os
from PIL import Image
from pytesseract import image_to_string
import pytesseract

browser = webdriver.PhantomJS()

# 显示等待时间10秒
wait = WebDriverWait(browser, 10)
base_url = 'http://my.cnki.net/elibregister/'

# 1。下载网页
def index_page(url):
    browser.get(url)
    # 验证码标签img加载完毕
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.register-box .dynamic-pic img')))
    html = browser.page_source
    # print(html)
    doc = pq(html)
    img = doc('.register-box .dynamic-pic img')
    print(base_url+img.attr('src'))
    save_image(base_url+img.attr('src'))


# 2。保存图片
def save_image(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:
        file_name = 'code.png'
        with open(file_name, 'wb') as fp:
           fp.write(response.content)
        # verify_yzm(file_name)
        verify_image(file_name)


# 3。验证图片一( 推荐 )
def verify_yzm(filename):
    f1, f2 = os.path.splitext(filename)

    calc_result = None
    try:
        im = Image.open(filename)

        # 1.切掉四周的黑边
        width = im.size[0]
        height = im.size[1]
        left = 4
        top = 4
        right = width - 4
        bottom = height - 4
        box = (int(left), int(top), int(right), int(bottom))
        im = im.crop(box)
        im = im.resize((width * 4, height * 4), Image.BILINEAR)
        im.save(f1 + '_step1' + f2)

        # 2.转为灰度图（转为灰度图才能二值化-去噪）
        imgry = im.convert('L')
        imgry.save(f1 + '_step2' + f2)

        # 3.去噪( 去除干扰的线条, 使整个验证码变的黑白分明 )
        threshold = 140
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        out = imgry.point(table, '1')
        out.save(f1 + '_step3' + f2)

        # 4.调用(将图片 转成 字符窜)
        text = image_to_string(out, config='-l eng')
        print('text: ', text)

        # 弹出/显示图片
        out.show()

    except Exception as e:
        print(e)
    return calc_result


# 4。验证图片二
def verify_image(file_name):
    image = Image.open(file_name)
    # 核心方法：pytesseract.image_to_string()
    print(pytesseract.image_to_string(image))
    image.show()


if __name__ == '__main__':
    url = 'http://my.cnki.net/elibregister/commonRegister.aspx#'
    index_page(url)