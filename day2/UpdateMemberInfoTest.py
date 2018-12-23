# 自己实现下面的测试用例脚本
# 1.登录
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("http://172.31.5.250/index.php?m=user&c=public&a=login")
driver.find_element_by_id("username").send_keys("changcheng")
driver.find_element_by_id("password").send_keys("123456")
# 我们可以用另一种方式避免定位登录按钮，达到直接登录的目的，可以用submir的方法
# submir是提交的意思，表单中所有数据是同时提交给服务器的
# 所以可以用表单中的任何一个元素提交整个表单
driver.find_element_by_id("password").submit()
# 2.点击“账号设置”
driver.find_element_by_link_text("账号设置").click()
# 3.点击“个人资料”
driver.find_element_by_partial_link_text("个人资料").click()
# 4.修改真实姓名
driver.find_element_by_id("true_name").clear()
driver.find_element_by_id("true_name").send_keys("常城")
# 5.修改性别
# find_element_by_css_selector的方法，可以用任意属性定位
# 只需要在属性的两边加一对中括号即可
driver.find_element_by_css_selector('[value="1"]').click()

# 6.修改生日
# 思路： 先去掉readonly属性，然后再输入生日
# 但是，selenium没有办法删除元素的任合属性
# 可以通过javascript删除readonly属性
# document.getElementById("date").removeAttribute("readonly")
# 上面这句是javascript的语句，不能直接在python环境中运行
# 要想在selenium中，执行javascript，需要调用execute_script()这个方法
driver.execute_script('document.getElementById("date").removeAttribute("readonly")')
# 在sendKeys之前，我需要删除输入框中的默认值，清空默认值的方法叫：clear
# 好的编程习惯，所有的输入框执行sendKeys之前，都要先清空输入框中的内容
driver.find_element_by_id("date").clear()
driver.find_element_by_id("date").send_keys("1980-03-04")
# 7.修改QQ
driver.find_element_by_id("qq").clear()
driver.find_element_by_id("qq").send_keys("242353456436435")
# 8.点击确定
driver.find_element_by_class_name("btn4").click()
# 弹出框的操作，必须要在前面加上一个时间等待，
# 这时隐式等待不起作用，因为隐式等待检查的是页面加载时间，
# 弹出框的出现，页面没有刷新，或者重新加载，所以隐式等待不起作用
time.sleep(2)
# driver.switch_to.alert.accept()  # 点击弹出框上的确定按钮
# driver.switch_to.alert.dismiss()  # 点击弹出框上的取消按钮
alert_text = driver.switch_to.alert.text   # 弹出框上显示的文本信息
print(alert_text)
driver.switch_to.alert.accept()

# 可以通过弹出框的文本信息，判断是否修改成功
if "个人信息修改失败！" == alert_text:
    print("测试通过")
else:
    print("测试失败")