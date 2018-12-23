# 1.打开浏览器
from selenium import webdriver
# 从 谷歌公司的一个项目 导入 网络驱动， 用代码来操作浏览器的
driver = webdriver.Chrome()
# 2.打开海盗商城主页
driver.get("http://172.31.5.250/")
# 3.输入关键词
driver.find_element_by_name("keyword").send_keys("iphone")
# 自动化测试的核心就两件事：1.元素定位，2.元素操作
# 元素定位就是找元素，selenium一共提供了8种方式找元素：1.name，后来还有7种，比如id，class。。。
# send_keys()发送键盘的按键
# 4.点击搜索按钮
driver.find_element_by_class_name("btn1").click()
# 5.检查结果是否正确
