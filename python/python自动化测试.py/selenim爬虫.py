from selenium import webdriver
import time
# 1.0 指定驱动的位置
# driver_path = r"./chromedriver.exe"

# 2.0 创建浏览器对象，并把驱动器的位置给这个对象
# browser = webdriver.Chrome(executable_path=driver_path)
# 
# --- options = webdriver.Chromeoptions() 
#     返回chrome的配置信息
#

################################### 设置代理
# 1.0 修改对应浏览器的配置信息
# options = webdriver.Chromeoptions()
# 2.0 配置代理信息 xxx 是代理ip
# options.add_argument("--proxy-server=xxxxx")
# 
# 3。0 把设置代理信息传递给 浏览器对象
# browder = webdriver.Chrome(executeble_path = driver_path, chrome_options = options)
 


#####################################请求方法
# 3.0 以get方法请求网址
# browser.get("http://www.baidu.com")








###################################### 网页源代码
#--- page_source() 获取网页源码









#################################### 定位元素和提取
# find_element_by_ *
# 1.0 如果定位元素是为了提取数据，我们可以用lxml解析，这样效率更高
# 2.0 如果我们需要队定位的元素，执行后续操作，我们需要用到他内置的定位方法

# 3.0 注意下面定位元素得方法如果在element后面加s 就说明是复数 可以获取多个元素，以列表的形式

# --- find_element_by_id('') 获取响应的id元素

# --- find_element_by_class_name('') 类名

# --- find_element_by_name('') name属性值

# --- find_element_by_xpath("")用xpath语法
# 
# --- find_element_by_link_text('') 用a标签的全部文本做匹配
# 
# --- find_element_by_partial_link_text('') 用a标签的部分文本做匹配
# 
# --- find_element_by_tag_name('') 按照标签名字来进行定位
# 
# --- find_element_by_css_selector('') 可以用css选择器来进行定位
# 
# 
# 
# 
# **************************** By类定位元素
# 这是两个私有方法：find_element和find_elements
# 用这个类 可能比较方便 ,他需要线规定By类里面的查询方法，
# 然后在后面写 查询的 元素
# from selenium.webdriver.common.by import By
# 下面列出By类 的查询方法：
# ID = "id"  # ID
# XPATH = "xpath" # XPATH
# LINK_TEXT = "link text" # 链接文本
# PARTIAL_LINK_TEXT = "partial link text" #部分链接文本
# NAME = "name" # 那么属性值
# TAG_NAME = "tag name" #标签名字
# CLASS_NAME = "class name" #类名
# CSS_SELECTOR = "css selector" # css选择器
# 
# --- find_element(By.ID,"xxx") #查询id

# --- find_elements("By.CLASS_NAME","xxx") #查询全部类名为xxx的元素
# 
# 
# 
# 
# 
# 
# 
############################################ 表单操作
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver import ActionChains
# from selenium.webdriver.support.ui import Select
# driver_path = r"./chromedriver.exe"
# brower = webdriver.Chrome(executable_path=driver_path)
# brower.implicitly_wait(10)
# brower.get("http://www.w3school.com.cn/tiy/t.asp?f=html_dropdownbox")
# input = brower.find_element(By.ID,"google_esf")
# select = 
# options = Select.options
# --- clear() 可以清除文本框

# --- setSelected 可以切换下拉列表 处理select 字段,我们可以引入一个类来操作select字段
# 
# from selenium.webdriver.support.ui import Select
# 
# select = Select(driver.find_element_by_name('name')) # 选取select表单 并创建一个select对象
# 
# select.select_by_index(index)  #他可以选区第几个option
# 
# select.select_by_visible_text("text") #选择指定文本的option
# 
# select.select_by_value(value) #选择value值 的option
# 
# select.deselect_all() #取消选择所有的 option
# 
# --- 获取所有的可用选项
# options = select.options
# 
# --- 获取所有默认选项的列表 
# all_selected_options = select.all_selected_options
# 
# 
# 
# 
# 
# **************** 当表单操作完成后,需要提交表单有两种方法
# 
# --- 选区表单 然后执行 click() 点击提交
# 
# --- 我们可以让表单的任意一个元素执行submit() 方法 他会自动找到他的表单 提交
# element.submit()
# 
# 
# 
# 
# 
# 
# 
######################################## 等待
#
# 如果页面存在大量的ajax 技术 那么通常无法准确的判断是否加载完毕
# 此时我们可以使用等待类，获取完成的数据
# 等待分为两种，一种为隐式等待 和 显式等待
# expected_conditions 包含一组用于WebDriverWait的预定义条件
# 
# title_is                                      # 判断当前页面的title是否精确等于预期
# title_contains                                # 判断当前页面的title是否包含预期字符串
# presence_of_element_located                   # 判断某个元素是否被加到了dom树里，并不代表该元素一定可见
# visibility_of_element_located                 # 判断某个元素是否可见.可见代表元素非隐藏，并且元素的宽和高都不等于0
# visibility_of                                 # 跟上面的方法做一样的事情，只是上面的方法要传入locator，这个方法直接传定位到的element就好了
# presence_of_all_elements_located              # 判断是否至少有1个元素存在于dom树中。举个例子，如果页面上有n个元素的class都是'column-md-3'，那么只要有1个元素存在，这个方法就返回True
# text_to_be_present_in_element                 # 判断某个元素中的text是否包含了预期的字符串
# text_to_be_present_in_element_value           # 判断某个元素中的value属性是否包含了预期的字符串
# frame_to_be_available_and_switch_to_it        # 判断该frame是否可以switch进去，如果可以的话，返回True并且switch进去，否则返回False
# invisibility_of_element_located               # 判断某个元素中是否不存在于dom树或不可见
# element_to_be_clickable                       # 判断某个元素中是否可见并且是enable的，这样的话才叫clickable
# staleness_of                                  # 等某个元素从dom树中移除，注意，这个方法也是返回True或False
# element_to_be_selected                        # 判断某个元素是否被选中了,一般用在下拉列表
# element_selection_state_to_be                 # 判断某个元素的选中状态是否符合预期
# element_located_selection_state_to_be         # 跟上面的方法作用一样，只是上面的方法传入定位到的element，而这个方法传入locator
# alert_is_present                              # 判断页面上是否存在alert
# 
# *************** 显式等待
# 他将设置一个最大的等待时间 如果在规定时间内返回 就可以了
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver_path = r"./chromedriver.exe"
# brower = webdriver.Chrome(driver_path)
# brower.get("http://www.baidu.com")
# try:
#     element = WebDriverWait(brower, 10).until(
#         EC.presence_of_element_located((By.ID, "kw1"))
#     )
# except:
#     pass    
# else:
#     print(element)
# finally:
#     brower.quit(）
#      
# ************** 隐式等待
# 他将driver设置为隐式等待，当没有可用的任何元素 那么他会轮询DOM 
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver_path = "./chromedriver.exe"
# brower = webdriver.Chrome(executable_path=driver_path)
# brower.implicitly_wait(10)
# brower.get("http://www.baidu.com")
# try:
#     element = brower.find_element(By.ID,"kw")
#     element1 = brower.find_element(By.CLASS_NAME,"s_iptss")
# except Exception as e:
#     raise e
# else:
#     print(element)
#     print(element1)
# finally:
#     brower.quit()



######################################## 鼠标操作
#
# --- click() 相当于点击点击
# --- context_click(elem) 右击鼠标点击元素elem，另存为等行为
# --- double_click(elem) 双击鼠标点击元素elem，地图web可实现放大功能
# --- drag_and_drop(source,target) 拖动鼠标，源元素按下左键移动至目标元素释放
# --- move_to_element(elem) 鼠标移动到一个元素上
# --- click_and_hold(elem) 按下鼠标左键在一个元素上
# --- perform() 在通过调用该函数执行ActionChains中存储行为
#
# 
# 
# 
# 
# 
# ######################################键盘操作
# from selenium.webdriver.common.keys import Keys
# --- end_keys(Keys.ENTER) 按下回车键
# --- send_keys(Keys.TAB) 按下Tab制表键
# --- send_keys(Keys.SPACE) 按下空格键space
# --- send_keys(Kyes.ESCAPE) 按下回退键Esc
# --- send_keys(Keys.BACK_SPACE) 按下删除键BackSpace
# --- send_keys(Keys.SHIFT) 按下shift键
# --- send_keys(Keys.CONTROL) 按下Ctrl键
# --- send_keys(Keys.ARROW_DOWN) 按下鼠标光标向下按键
# --- send_keys(Keys.CONTROL,'a') 组合键全选Ctrl+A
# --- send_keys(Keys.CONTROL,'c') 组合键复制Ctrl+C
# --- send_keys(Keys.CONTROL,'x') 组合键剪切Ctrl+X
# --- send_keys(Keys.CONTROL,'v') 组合键粘贴Ctrl+V
# 
# 
# 
# #################################### 行为链
# 他可以执行连续性的操作
# from selenium.webdriver import ActionChains
# 
# 1.0 创建一个行为链对象 
# action = ActionChains(brower)
# 
# 2.0 然后用action来模拟浏览器一系列连续的动作
# action.click() 
# 
# 
# 
# 
# 
# 
# 
# ################################### 执行javascript 代码
# 
# driver.execute_script("") #他专门执行javascript 代码
# 
# 
# 
# 
###################################### 拖放元素
#
# 拖放元素需要用到这个 from selenium.webdriver import ActionChains
# 
# 1.0 创建一个移动对象
# action_chains = ActionChains(driver)
# 
# 2.0 然后把element 元素 移动到target 位置    
# action_chains.drag_and_drop(element, target).perform() 
# 
# 
# 
# 
# 
# 
# 
##################################### 窗口和框架之间的移动
# 
# driver.switch_to_window("windowName") 可以移动到特定的窗口
#
# --- 我们可以遍历所有窗口 来获得每一个窗口
# for handle in driver.window_handles:
# 
# 
# --- 切换到指定的页面
#   driver.switch_to_window(handle) 
#   
#   
# --- driver.current_url  返回当前页面的url
# 
# 
# --- 移动到指定的框架
# driver.switch_to_frame("frameName")
# 
# --- 可以用点语法或者索引来指定框架内部的第几个子框架
#     child frameName 内的第一个框架
# driver.switch_to_frame("frameName.0.child") 

# --- 完成框架内部的操作后回到主框架
# driver.switch_to_default_content()
# 
# 
# 
# 
# 
# 
# ################################## 弹出会话框的操作
# 
# --- 返回一个弹出框对象
# alert = driver.switch_to_alert()
# 
# 
# 
# 
# 
# 
# 
# ################################ 浏览器的导航和历史记录
# 
# 导航相当于 浏览器的上一个页面和下一个页面
# driver.forward() #往前
# driver.back() #往后移动
# 
# 
# 
# ############################### 浏览器的设置
# 
# 
# 
# 
# ################################cookie 操作
# 
# --- 设置cookie 
# cookie = {‘name’ : ‘foo’, ‘value’ : ‘bar’}
# driver.add_cookie(cookie)
# 
# --- 获取cookie 
# driver.get_cookies('key')
# 
# --- 删除cookie
# driver.delete_cookies()
# 
# --- 删除全部cookies
# driver.delete_all_cookies()
# 
# 
# 
# 
# 
# 
####################################### 键盘输入
#
# --- send_keys('') 在input text类型里输入文字
# inputTag.send_keys("你好")




##################################### 关闭网页和浏览器
#
# --- cloce() 关闭当前页面
# --- quit() 关闭浏览器
# time.sleep(2)
# browser.quit()
# 
# 
# 
# ################################## 面向对象设计模式
# 
# 