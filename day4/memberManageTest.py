import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class MemberManageTest(unittest.TestCase):
    # @classMethod是一个注解，作用是给下面的方法提供一些特殊的特性
    #     @classmethod的作用类似静态方法，不需要实例化就可以直接调用的方法
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        time.sleep(30)
        cls.driver.quit()

    def test_1_login(self):
        driver = self.driver
        driver.get("http://172.31.5.250/index.php?&m=admin&c=public&a=login")
        # 添加会员的剩余步骤，自己实现
        # 1.登录
        driver.find_element_by_name("username").send_keys("admin")
        ActionChains(driver).send_keys(Keys.TAB).send_keys("password").send_keys(Keys.TAB).send_keys("1234").send_keys(Keys.ENTER).perform()

    def test_2_member_adding(self):
        driver = self.driver
        # 2.点击"会员管理"
        driver.find_element_by_link_text("会员管理").click()
        # 3.点击左侧的添加会员
        driver.find_element_by_link_text("添加会员").click()
        # 4.输入会员信息
        driver.switch_to.frame("mainFrame")
        driver.find_element_by_name("username").send_keys("薛之谦")
        driver.find_element_by_name("mobile_phone").send_keys("13121378945")
        driver.find_elements_by_name("sex")[0].click()
        driver.find_element_by_id("birthday").send_keys("1981-03-24")
        driver.find_element_by_name("email").send_keys("wfwfefegreg@163.com")
        driver.find_element_by_name("qq").send_keys("2343253465")
        # 5.点击提交按钮
        driver.find_element_by_class_name("button_search").click()

# 表示下面这段代码是程序的入口，不会被其他方法调用
# 输入“main”，然后敲回车
# 这句话要求定格写
if __name__ == '__main__':
    unittest.main()