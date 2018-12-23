# 1.登录
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("http://172.31.5.250/index.php?m=admin&c=public&a=login")
driver.find_element_by_name("username").send_keys("admin")
# 假如密码输入框不容易定位，可以用另一种方式输入密码
# 模仿输入tab键，直接切换到密码框
# Action是动作行为的意思，我们对页面元素的所有操作都是Action
# Chains是链表的意思，表示这是一组动作行为
# 那么这组动作发生在当前的浏览器上，所以要把driver传进去
# perform表示执行，ActionChains的方法链表必须以perform结尾，才会真正执行
ActionChains(driver).send_keys(Keys.TAB).send_keys("password").send_keys(Keys.TAB).send_keys("1234").send_keys(Keys.ENTER).perform()
# 2.点击“商品管理”
driver.find_element_by_link_text("商品管理").click()
# 3.点击“添加商品”
driver.find_element_by_link_text("添加商品").click()
# 4.输入商品名称
# driver.find_element_by_name("name").send_keys("诺基亚")
# /html/body/div[2]/div[2]/dl/form/dd[1]/ul/li[1]/input
# driver.find_element_by_xpath("/html/body/div[2]/div[2]/dl/form/dd[1]/ul/li[1]/input").send_keys("诺基亚")
# 这种页面是嵌套网页，我们需要切换网页
driver.switch_to.frame("mainFrame")
driver.find_element_by_name("name").send_keys("诺基亚")
# 5.选择商品分类
driver.find_element_by_id("1").click()
driver.find_element_by_id("2").click()
driver.find_element_by_id("6").click()
# driver.find_element_by_id("7").click()
ActionChains(driver).double_click(driver.find_element_by_id("7")).perform()
# 6.选择商品品牌
brand_id = driver.find_element_by_name("brand_id")
Select(brand_id).select_by_index(1)
# 7.点击提交按钮
# driver.find_element_by_class_name("button_search").click()
# 点击提交按钮之前，先上传一张商品图片，
# 1.点击商品图册
driver.find_element_by_link_text("商品图册").click()

# driver.find_element_by_xpath('//*[@id="rt_rt_1cuo65id8136211ct68gn7v1tci8"]/label')
# css语法知识： 1.所有的属性都可以通过两边加中括号的方式定位
# 2.属性的键和值之间用=等号表示相等
# 3.属性的键和值之间用|=表示选择以rt_rt开头的页面元素
# 4.大于号表示父节点和子节点之间的关系

driver.find_element_by_name("file").send_keys("D:/AddProductImg.png")
# 点击开始上传按钮
# driver.find_element_by_class_name("uploadBtn state-finish state-ready")
# find_element_by_class_name(）方法不能用组合的className
# 但是cssSelector()这个方法可以用组合的属性
# 在css中class属性有两种表示方法
driver.find_element_by_css_selector(".uploadBtn.state-finish.state-ready").click()
#处理弹出框
time.sleep(5)
uploadSuccess = driver.switch_to.alert.text
driver.switch_to.alert.accept()
if(uploadSuccess == "上传成功"):
    print("测试用例执行成功")
else:
    print("测试用例执行失败")
# driver.find_element_by_id("uploadSuccess").click()










