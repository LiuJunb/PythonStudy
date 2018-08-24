from selenium import webdriver

# browser = webdriver.Chrome()
browser = webdriver.PhantomJS()
url = 'https://www.zhihu.com/explore'
browser.get(url)
input = browser.find_element_by_class_name('zu-top-add-question')

print(input)
# element=":wdc:1535011697120")
print(input.id)  # :wdc:1535011570191
print(input.location)  # {'x': 163, 'y': 7}
print(input.tag_name)  # button
print(input.size)  # {'height': 32, 'width': 66}