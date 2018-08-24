import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
# 连续打开两个窗口（ 共3个窗口 ）
browser.execute_script('window.open()')
browser.execute_script('window.open()')
# ['CDwindow-76F9F7556621FBE73D65CBDB3B3365DA',
# 'CDwindow-C68CAC83684E18871EDE580F3E01A195',
# 'CDwindow-F4D29D92B3965BCE010ACF10F0AE3BCE']
print(browser.window_handles)

browser.switch_to_window(browser.window_handles[1])
browser.get('https://www.taobao.com')
time.sleep(1)
browser.switch_to_window(browser.window_handles[0])
browser.get('https://www.jd.com')
time.sleep(1)
browser.switch_to_window(browser.window_handles[2])
browser.get('https://www.mi.com/')