# 之前登录的时候，我要求，直接打开登陆页面
# 现在，我要求，先打开主页，然后点击右上角的登录按钮，然后再执行登陆录
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://172.31.5.250/")
driver.find_element_by_link_text("登录").click()
# driver.find_element_by_id("username").send_keys("changcheng")
# driver.find_element_by_name("keyword").send_keys("iphone")

# 窗口切换
# selenium默认在第一个窗口工作
# 当我们点击某些链接时会弹出新窗口
# 这时我们要切换窗口--如何让selenium在新的窗口上工作？
# 1.selenium提供了切换窗口的方法
# driver.switch_to.window(第二个窗口的名字)
# 2.找出第二个窗口的名字
# driver的windowHandles属性，可以获取浏览器中所有的窗口名字
# driver.window_handles[1]
# 如果我不知道当前浏览器有几个窗口，我就切换到最新的，最新的是-1
driver.switch_to.window(driver.window_handles[-1])

driver.find_element_by_id("username").send_keys("changcheng")