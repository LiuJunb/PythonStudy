from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
# selenium.common.exceptions.NoSuchElementException: Message: no such element: 
browser.find_element_by_id('hello')