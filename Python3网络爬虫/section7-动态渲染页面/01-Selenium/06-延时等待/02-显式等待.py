from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

# 执行到17行会报错
# browser = webdriver.PhantomJS()
browser.get('https://www.taobao.com/')


# 指定好最长等待时间10 秒
wait = WebDriverWait(browser, 10)
# 等待条件presence_of_element_located(就代表节点出现的意思)
input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))

# 上面显示等待： 做到的效果就是，在 10 秒内如果 ID 为 q 的节点即搜索框成功加载出来了，那就返回该节点，如果超过10 秒还没有加载出来，那就抛出异常


print(input, button)