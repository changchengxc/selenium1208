# 在这个文件中，把我们以前写的测试用例，改写成基于unittest的测试用例
import time
import unittest
from selenium import webdriver

# 1.继承父类TestCase
class LoginTest2(unittest.TestCase):
    # 2.重写setUp和tearDown
    def setUp(self):
        # 在方法内部声明的变量只能用于当前方法
        # 要想让其他方法访问变量driver，必须在driver前面加上self关键字，表示driver是属于类的
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def tearDown(self):
        time.sleep(30)
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        driver.get("http://172.31.5.250/")
        driver.find_element_by_link_text("登录").click()
        self.switch_window()
        driver.find_element_by_id("username").send_keys("changcheng")

    def switch_window(self):
        new_window = self.driver.window_handles[-1]
        self.driver.close()
        self.driver.switch_to.window(new_window)