from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')

# 1.通过id查找节点
input_first = browser.find_element_by_id('q')
# input_first = browser.find_element(By.ID, 'q')

# 2.通过选择器查找
input_second = browser.find_element_by_css_selector('#q')
# 3.通过xPath查找 （ / //  .  ..  []   @ ）
input_third = browser.find_element_by_xpath('//*[@id="q"]')

print(type(browser))
print(type(input_first))  # <class 'selenium.webdriver.remote.webelement.WebElement'>
print(input_first, input_second, input_third, sep='\n')

browser.close()

# find_element_by_id
# find_element_by_name
# find_element_by_class_name
# find_element_by_tag_name
# find_element_by_css_selector
# find_element_by_xpath

# find_element_by_link_text
# find_element_by_partial_link_text

