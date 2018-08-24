from selenium import webdriver

browser = webdriver.Chrome()
# 1.打开这个网页
browser.get('https://www.zhihu.com/explore')

# 2.打开后执行一个js脚本
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')


