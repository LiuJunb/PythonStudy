import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# 1.使用这个会报错
# browser = webdriver.PhantomJS()
browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
try:
    logo = browser.find_element_by_class_name('logo')
except NoSuchElementException:
    print('NO LOGO')

browser.switch_to.parent_frame()
logo = browser.find_element_by_class_name('logo')

print(logo)
print(logo.text)