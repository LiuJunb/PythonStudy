from selenium import webdriver

browser = webdriver.Chrome()
# 访问淘宝页面
browser.get('https://www.taobao.com')
# 拿到网页的源码
print(browser.page_source)

browser.close()