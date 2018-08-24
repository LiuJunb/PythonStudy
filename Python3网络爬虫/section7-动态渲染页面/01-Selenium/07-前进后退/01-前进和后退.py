import time
from selenium import webdriver

browser = webdriver.Chrome()
# browser = webdriver.Firefox()
browser.get('https://www.baidu.com/')
browser.get('https://www.taobao.com/')
browser.get('https://www.jd.com/')

# 在当前窗口进行页面跳转

# 后退( 在页面加载完之后才能会执行 )
time.sleep(1)
browser.back()
time.sleep(1)
# 前进
browser.forward()
# browser.close()