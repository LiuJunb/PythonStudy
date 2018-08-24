from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')

# 1.获取cookie
print(browser.get_cookies())
# 2.添加 一个 cookie
browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
# 3.获取cookie
print(browser.get_cookies())

# browser.delete_all_cookies()
#
# print(browser.get_cookies())



