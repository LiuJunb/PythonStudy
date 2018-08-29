from selenium import webdriver

proxy = '120.24.152.123:3128'  # 可用https
# proxy = '111.155.116.234:8123'  # 可用 http

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://' + proxy)
# 拿到浏览器对象
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('http://httpbin.org/get')











