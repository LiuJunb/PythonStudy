from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
    input = browser.find_element_by_id('kw')
    input.send_keys('Python')
    # 1.自动模拟按回车键
    input.send_keys(Keys.ENTER)

    # 等待 10 ms
    # wait = WebDriverWait(browser, 10)

    # 等待 content_left 这个id 出现 才继续往下执行
    # wait.until(EC.presence_of_element_located((By.ID, 'content_left')))

    # 获取当前的网页
    print(browser.current_url)
    # 获取网页的cookie
    # print(browser.get_cookies())
    # 获取网页的源码
    # print(browser.page_source)

finally:
    # 关闭浏览器
    # browser.close()
    pass