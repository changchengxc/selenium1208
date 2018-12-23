import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from day4.readCsvFile import read


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
        data = read()
        for row in data:
            driver = self.driver
            # 2.点击"会员管理"
            # driver.switch_to.parent_frame()   # 表示返回上一级frame
            driver.switch_to.default_content()  # 表示页面根节点
            driver.find_element_by_link_text("会员管理").click()
            # 3.点击左侧的添加会员
            driver.find_element_by_link_text("添加会员").click()
            # 4.输入会员信息
            driver.switch_to.frame("mainFrame")

            driver.find_element_by_name("username").send_keys(row[0])
            driver.find_element_by_name("mobile_phone").send_keys(row[1])
            if "男" == row[2]:
                driver.find_elements_by_name("sex")[0].click()
            elif "女" == row[2]:
                driver.find_elements_by_name("sex")[0].click()
            else:
                print("csv文件中数据不正确，性别只支持男或者女")
            driver.find_element_by_id("birthday").send_keys(row[3])
            driver.find_element_by_name("email").send_keys(row[4])
            driver.find_element_by_name("qq").send_keys(row[5])
            # 5.点击提交按钮
            driver.find_element_by_class_name("button_search").click()
            time.sleep(3)
            # 通过xpath找到页面元素以后，加.text可以获取元素的文本信息
            # 通过执行测试，在结果页面中获取的网页信息就是测试的实际结果
            actual_result = driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[1]/div').text
            # 接下来，用实际结果和期望结果比较
            # 期望结果是测试执行前，写在csv文件中的数据
            # if row[6] == actual_result:
            #     print("测试用例成功")
            # else:
            #     print("测试用例失败")
#             用if....else判断测试用例是否成功，不是专业的写法，应该使用断言来判断测试用例是否成功
#           断言的英文叫assert，作用类似于if...else...
#             用一句断言，就代替了4句，所以断言更简介
#             如果测试用例通过，断言不会打印任何信息，只有测试用例失败，才会打印详细的日志
#             如果测试用例中间执行失败，断言后面的语句不会继续执行了
#             我们需要一个ddt数据驱动测试框架，把这条测试用例，根据csv文件中行数，分成多个测试用例

            self.assertEqual("常城", actual_result)

# 表示下面这段代码是程序的入口，不会被其他方法调用
# 输入“main”，然后敲回车
# 这句话要求定格写
if __name__ == '__main__':
    unittest.main()

# 我们现在可以批量添加会员了，但是有一个问题：
# 在循环中其中有一条测试用例执行失败，抛出了异常，那么剩余的测试用例还可不可以正常执行?