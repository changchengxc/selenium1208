import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class MemberHubPage:
    loc_welcome_link = (By.CSS_SELECTOR, "div.site-nav-right.fr > a:nth-child(1)")

    def __init__(self, driver):
        self.driver = driver

    def get_welcome_text(self):
        time.sleep(3)
        return self.driver.find_element(*self.loc_welcome_link).text
