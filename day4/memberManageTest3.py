import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
# 1.导入ddt
import ddt
from day4.readCsvFile2 import read


#2.给测试用例类增加一个装饰器,表示当前类使用了ddt框架作为数据驱动的底层
@ddt.ddt
class MemberManageTest(unittest.TestCase):

    # 3.读取csv文件的内容
    data = read("testdata.csv")

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

# 4.把csv文件中的数据传给测试用例方法
    # data的类型是列表，就是我们在read()方法中声明的list=[]
    # *data表示的是列表中的每个元素，这里每个元素，就表示csv中的每行数据
    @ddt.data(*data)
    def test_2_member_adding(self,row):
        driver = self.driver
        # 2.点击"会员管理"
        driver.switch_to.default_content()
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
            driver.find_elements_by_name("sex")[1].click()
        else:
            print("性别输入有误，只支持男或者女")
        driver.find_element_by_id("birthday").send_keys(row[3])
        driver.find_element_by_name("email").send_keys(row[4])
        driver.find_element_by_name("qq").send_keys(row[5])
        # 5.点击提交按钮
        driver.find_element_by_class_name("button_search").click()
        time.sleep(3)
        actual_result = driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[1]/div').text
        self.assertEqual(row[6],actual_result)

# 表示下面这段代码是程序的入口，不会被其他方法调用
# 输入“main”，然后敲回车
# 这句话要求定格写
if __name__ == '__main__':
    unittest.main()