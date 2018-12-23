import time
import unittest
from selenium import webdriver


class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        # 在编写和调试代码阶段，time.sleep()可以帮助我们更清楚的观察测试结果
        # 代码稳定和完成以后，再去掉这个time.sleep()
        time.sleep(10)
        cls.driver.quit()
        # 以后，其他测试用例只要继承BaseTestCase这个类，就继承了这个类的setUp和tearDown方法
        # 以后，其他测试用例就不需要再重新写这setUp和tearDown方法了
