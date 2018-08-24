from selenium import webdriver

# browser = webdriver.Chrome()
browser = webdriver.PhantomJS()
url = 'https://www.zhihu.com/explore'
browser.get(url)

# 1.获取 WebElement 对象
input = browser.find_element_by_class_name('zu-top-add-question')
# 2.调用对象中国中的text属性
print(input.text)




