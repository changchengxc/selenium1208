from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://172.31.5.250/")
driver.find_element_by_css_selector("div.site-nav-right.fr > :nth-child(2)").click()