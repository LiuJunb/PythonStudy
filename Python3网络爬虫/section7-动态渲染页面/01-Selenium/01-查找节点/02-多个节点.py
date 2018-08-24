from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')

lis = browser.find_elements_by_css_selector('.service-bd li')
print(lis, sep='\n')

browser.close()


# find_elements_by_id
# find_elements_by_name
# find_elements_by_tag_name
# find_elements_by_class_name
# find_elements_by_css_selector
# find_elements_by_xpath

# find_elements_by_link_text
# find_elements_by_partial_link_text
