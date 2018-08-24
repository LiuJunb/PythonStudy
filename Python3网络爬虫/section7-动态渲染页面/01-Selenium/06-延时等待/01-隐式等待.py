from selenium import webdriver

browser = webdriver.PhantomJS()
# 1.如果 Selenium 没有在DOM 中找到节点，将继续等待，超出设定时间后则抛出找不到节点的异常
browser.implicitly_wait(10)

browser.get('https://www.zhihu.com/explore')
input = browser.find_element_by_class_name('zu-top-add-question')
print(input)