from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
url = 'https://www.zhihu.com/explore'
browser.get(url)

# 1.拿到 WebElement 对象（ 是a标签 ）
logo = browser.find_element_by_id('zh-top-link-logo')
# <selenium.webdriver.remote.webelement.WebElement
# (session="edbf8a6ee434863882f7e312b67da3a0", element="0.05464593363911607-1")>
print(logo)
# 2.调用 WebElement 中的方法来获取属性
print(logo.get_attribute('class'))




