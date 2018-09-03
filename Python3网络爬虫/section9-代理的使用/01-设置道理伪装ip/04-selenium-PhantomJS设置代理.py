from selenium import webdriver

# proxy = '120.24.152.123:3128'  # 可用https
# proxy = '111.155.116.234:8123'  # 可用 http

service_args = [
    '--proxy=120.24.152.123:3128',
    '--proxy-type=http'
]

browser = webdriver.PhantomJS(service_args=service_args)

browser.get('http://httpbin.org/get')

print(browser.page_source)











