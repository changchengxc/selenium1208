import time
import unittest
from selenium import webdriver
import ddt
# 用来测试注册功能的所有异常情况
from day5.baseTestCase import BaseTestCase
from day5.readCsvFile import read


@ddt.ddt
class RegisterTest(BaseTestCase):

    register_data = read("register_data.csv")

    @ddt.data(*register_data)
    def test_register(self, row):
        driver = self.driver
        driver.get("http://172.31.5.250/index.php?m=user&c=public&a=reg")
        driver.find_element_by_name("username").send_keys(row[0])
        driver.find_element_by_name("password").send_keys(row[1])
        driver.find_element_by_name("userpassword2").send_keys(row[2])
        driver.find_element_by_name("mobile_phone").send_keys(row[3])
        driver.find_element_by_name("email").send_keys(row[4])
        driver.find_element_by_class_name("reg_btn").click()
# 定位所有的错误提示信息：
#         body > div.w1180 > div > div.reg_main > div.reg_left.fl > form > ul > li:nth-child(1) > div > span
#         body > div.w1180 > div > div.reg_main > div.reg_left.fl > form > ul > li:nth-child(2) > div > span
#         body > div.w1180 > div > div.reg_main > div.reg_left.fl > form > ul > li:nth-child(3) > div > span
#         range是取值范围的意思。
#         range(1,6)表示i的取值是1到5
        # 断言
        time.sleep(2)
        for i in range(1,6):
            # 用户名的校验信息，在网页上是第一个；密码的校验信息，在网页上是第二个
            # csv文件中存放的是期望结果，来自于需求文档，用户名的校验信息，在csv中是第6列，所以j=i+4
            element = driver.find_element_by_css_selector("form.registerform.sign > ul > li:nth-child(" + str(i) + ") > div > span")
            j = i + 4
            self.assertEqual(row[j], element.text)


if __name__ == '__main__':
    unittest.main()
    # 因为所有的测试用例，都要写setUp和tearDown方法，我们为了避免重复代码，打开浏览器和关闭浏览器的代码应该只写一次
    # 如何只写一次打开浏览器和关闭浏览器，就让所有的测试用例都生效？