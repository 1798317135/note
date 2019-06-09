from selenium import webdriver

# 提供键盘按键的支持
# from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# 请求网址
driver.get('https://www.douban.com/')
# 隐式等待 10 秒 其实是10秒之内的实际完成时间
driver.implicitly_wait(10) # seconds
driver.find_element_by_id('form_email').clear()
driver.find_element_by_id("form_email").send_keys("760008395@qq.com")
driver.implicitly_wait(2)
driver.find_element_by_id("form_password").send_keys("b123456789")
driver.find_element_by_css_selector("input.bn-submit").click()
# 查找标签名
# element = driver.find_element_by_name("passwd")