from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://172.31.5.250/index.php")
# 在点击登录按钮之前，先删除按钮的target属性
# script = 'document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")'
# driver.execute_script(script)
# # 执行脚本后，点击链接
# driver.find_element_by_link_text("登录").click()
# driver.find_element_by_id("username").send_keys("changcheng")
# 在这段代码中，我们分别用js和selenium定位了登录按钮，每次重新找这个页面元素都要花时间，那么我们可不了可以只找一次
# 比如，只用javascript方式查找元素，或者只用selenium方式查找元素，供两个地方一起使用
# 第一种方法，通过selenium定位：
# login_link = driver.find_element_by_link_text("登录")
# login_link ==  document.getElementsByClassName("site-nav-right fr")[0].childNodes[1]
# login_link和document.getElementsByClassName("site-nav-right fr")[0].childNodes[1]指的是同一个网页元素
# 接下来要做的就是把login_link传入java_script脚本中
# 要想把login_link这个页面元素传入到javascript中，要使用关键字：arguments[0]
# driver.execute_script("arguments[0].removeAttribute('target')", login_link)
# driver.execute_script("arguments[0].removeAttribute(arguments[1])", login_link, 'target')
# login_link.click()
# driver.find_element_by_id("username").send_keys("changcheng")
# 另一种方法，通过javascript定位：这个不是很常用，但是很适合面试的时候讲
script = 'return document.getElementsByClassName("site-nav-right fr")[0].childNodes[1]'
# 接下来只要把这段字符串转成网页元素类型就可以了
# 这里也需要一个关键词： return， 要想通过执行javascript返回网页元素，那么需要在网页元素前加一个return关键字
login_link = driver.execute_script(script)
login_link.click()