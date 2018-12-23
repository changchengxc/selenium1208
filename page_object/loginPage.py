from selenium import webdriver
from selenium.webdriver.common.by import By

from page_object.memberHubPage import MemberHubPage


class LoginPage:
    # 类中分为属性和方法两部分
    # selenium中最重要的就是元素的定位和元素的操作
    # 测试用例中可能会用到哪些元素，就写哪些元素
    # 1.用户名输入框的定位
    loc_username_input = (By.ID, "username")
    # 2.密码输入框的定位
    loc_password_input = (By.ID, "password")
    # 3.登录按钮的定位
    loc_login_button = (By.CLASS_NAME, "login_btn")
    # 4.网址
    url = "http://172.31.5.250/index.php?m=user&c=public&a=login"

    # driver = webdriver.Chrome()
    # 使用setUp方法中创建好的浏览器
    # 为方法写一个构造函数，把driver传进来
    def __init__(self, driver):
        self.driver = driver

    # 1.打开页面
    def open(self):
        self.driver.get(self.url)
    # 2.输入用户名
    def input_username(self, username):
        self.driver.find_element(*self.loc_username_input).send_keys(username)
    # 3.输入密码
    def input_password(self, password):
        self.driver.find_element(*self.loc_password_input).send_keys(password)
    # 4.点击登录按钮
    def click_login_button(self):
        self.driver.find_element(*self.loc_login_button).click()
        return MemberHubPage(self.driver)