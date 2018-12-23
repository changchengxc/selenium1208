# 前提：自己注册账号
# 使用网址直接打开登录页面：http://172.31.5.250/index.php?m=user&c=public&a=login
# 不要点登录链接
# 和search类似，需要你们自己实现登录功能

# 1.打开浏览器
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# 智能等待
driver.implicitly_wait(5)
# 隐式等待有两个特点
# 第一个： 只需要写一次，对后面所有代码都生效
# 第二个： 自动化判断应该等几秒，页面一旦加载完成，就立刻进行后面的操作，不会有时间浪费
# implicitly_wait括号中的数字表示，最大的等待时间，超过最大时间，直接报错
# 2.打开登录页面
driver.get("http://172.31.5.250/index.php?m=user&c=public&a=login")
# 3.输入用户名
driver.find_element_by_id("username").send_keys("changcheng")
# 4.输入密码
driver.find_element_by_id("password").send_keys("123456")
# 5.点击登录按钮
driver.find_element_by_class_name("login_btn").click()
# 6.点击进入商城购物
# 点击登录后，首先进入”成功“页面，在成功页面直接找这个链接找不到
# 应该让我们的程序等待几秒之后，再开始查找一个链接
# 光标点击Alt加回车，选择import this name， 选择time
# time.sleep(3)
driver.find_element_by_link_text("进入商城购物").click()
# 第5种元素定位方法：xpath
# /html/body/div[3]/div[1]/....
# /html/body/div[5]/div/div[2]/div[1]/a/img
driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div[1]/a/img").click()
#  今天下午的主要目的，就是把前端的购物流程讲完，从登录到结算整个业务场景
# 7.点击商品详情页的”加入购物车“
# handles是句柄，和名字，id这些类似，是浏览器窗口的一个标识
# handles的s表示的是所有的窗口，0表示第一个， 1表示第二个， -1表示倒数第一个，-2表示倒数第二个
# 如果我们想选最后一个，最新的那个，一般用-1表示
driver.switch_to.window(driver.window_handles[-1])
driver.find_element_by_id("joinCarButton").click()
#  8.点击”去购物车结算“
# time.sleep(3)
# 为了提高程序执行的稳定性，我们在这里需要加一个time.sleep()
# 但是有的时候，我们很难确定什么情况应该加time.sleep()
# 如果有所有链接前都加time.sleep(3)，那么无疑程序回变慢
# 如果该加的的地方不加，程序的稳定行就会变差
# 有一个一劳永逸的办法： 智能等待
# 现在等得都是固定时间，以后可以用智能等待自动判断是应该加时间等待
# 智能等待：只需要在程序最上方加 driver.implicitly_wait(10)

driver.find_element_by_class_name("shopCar_T_span3").click()
# 9.点击结算
driver.find_element_by_link_text("结算").click()
# 10，输入收货人地址
driver.find_element_by_class_name("add-address").click()
driver.find_element_by_name("address[address_name]").send_keys("常城")
driver.find_element_by_name("address[mobile]").send_keys("13823423123")
# 省
# 找到下拉框以后，要在下拉框中选择一个具体的省，这个操作不是click，更不是sendKeys，而是选择一个选项select
# 不是所有的网页元素，都需要一个select方法，所以网页元素这个类中只有click和sendKeys这些方法，没有select方法
# 思路： 所以，就需要我们自己写一个类，比如叫下拉框的类，让这个类继承网页元素类中的原有方法，并且再实现选择的方法
# 幸好，下拉框的类在selenium中已经帮我们写好了，不需要我们自己重新写
# 我们只需要把找出的页面元素，转换成下拉框的类型，就可以直接调用选择的方法了
sheng = driver.find_element_by_id("add-new-area-select")
Select(sheng).select_by_index(6)
# 市
# //*[@id="linkagesel_712984"]复制xpath也是不行的，因为xpath也是通过id属性定位的
# 第六种定位方式： tagName 通过标签名
# find_elements 表示所有符合条件的页面元素
# 这样就可以尝试找出所有标签名是select的页面元素了
# driver.find_elements_by_tag_name("select")
# 页面上一共三个下拉框，这样我们就可以通过下标进行选择了，选择第二个下拉框，就是中括号1
shi = driver.find_elements_by_tag_name("select")[1]
Select(shi).select_by_visible_text("铁岭市")
# 收货人信息的剩余部分自己完成
# 试试select_by_value方法
qu = driver.find_elements_by_class_name("add-new-area-select")[2]
Select(qu).select_by_value("211202")
