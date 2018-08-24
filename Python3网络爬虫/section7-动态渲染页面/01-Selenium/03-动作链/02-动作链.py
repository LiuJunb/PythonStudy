from selenium import webdriver
# 导入动作链
from selenium.webdriver import ActionChains

# 1.拿到浏览器
browser = webdriver.Chrome()

url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# 2.访问这个地址
browser.get(url)

# 更具iframe id 切换到对应的window窗口
browser.switch_to.frame('iframeResult')

source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')

# 3.拿到动作链
actions = ActionChains(browser)
# 4.指定拖拽原和目标
actions.drag_and_drop(source, target)
# 5.开始拖拽
actions.perform()