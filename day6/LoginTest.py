import os
import time

from day5.baseTestCase import BaseTestCase
from page_object.loginPage import LoginPage


class LoginTest(BaseTestCase):
    def test_login(self):
        # 1.实例化登录页面
        lp = LoginPage(self.driver)
        # 2.打开登录页面
        lp.open()
        # 3.输入用户名
        lp.input_username("changcheng")
        # 4.输入密码
        lp.input_password("123456")
        # 5.点击登录按钮
        mhp = lp.click_login_button()

        base_path = os.path.dirname(__file__)
        path = base_path.replace("day6","image/" + "登录成功.png")
        self.driver.get_screenshot_as_file(path)

        time.sleep(3)
        # welcome = self.driver.find_element_by_css_selector("div.site-nav-right.fr > a:nth-child(1)").text
        # print(welcome)
        print(self.driver.title)
        print(self.driver.current_url)
        print(self.driver.find_element_by_css_selector("div.site-nav-right.fr > a:nth-child(2)").get_attribute("href"))
        expected = mhp.get_welcome_text()
        self.assertEqual(expected, "您好 changcheng")
#         还可以加数据驱动测试，自己回去试试
        print("github 修改成功")



