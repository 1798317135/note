from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from queue import Queue
from lxml import etree
import time
import threading
import requests
import base64
import gevent
from gevent import monkey
import json
from PIL import Image
# monkey.patch_all()
class LagouSpider(threading.Thread):
    def __init__(self,city="全国"):
        super().__init__()
        self.driver_path = r"./chromedriver.exe"
        self.url = "https://www.lagou.com/"
        self.driver = None
        city_list = ["上海","北京","杭州","广州","深圳","成都","武汉","江苏","全国"]
        if city in city_list:
            self.city = city
        self.job = "python"
        self.options = webdriver.ChromeOptions()
        prefs = {
            'profile.default_content_setting_values' : {
                # 'images' : 2,
                'notifications' : 2
            }  
        }
        # self.options.add_argument('--headless')
        self.options.add_experimental_option('prefs',prefs)
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--disable-infobars")
        self.options.add_argument("--incognito")
        self.driver = webdriver.Chrome(executable_path = self.driver_path,options = self.options)
        # print(os.listdir())
        # with open("./qqhomepage.json","rb") as f:
        #     cookies = json.loads(f.read())
        # self.driver.add_cookie(cookies)
        # self.driver.maximize_window() #屏幕对大
        self.driver.set_window_size(1280, 1024) #设置窗口大小
        self.driver.implicitly_wait(5)
        self.q = Queue(100)
        self.timeout = WebDriverWait(self.driver,5)
        
        
    def run(self):
        self.index_page()
        self.list_page()


    def __call__(self,job):
        self.job = job


    def verfiy(self,img_path):
        headers = {"Content-Type":"application/x-www-form-urlencoded"}
        access_token = "24.8c9d19026505908d8705c746ced9a540.2592000.1557164899.282335-15948645"
        url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token=' + access_token
        with open(img_path,"rb") as f:
            img = base64.b64encode(f.read())
        data =  {
            "image":img
        }
        response = requests.post(url, headers=headers, data=data)
        content = response.json()
        if content["words_result_num"] == 1:
            content = content["words_result"][0]["words"]
        else:
            content = "abcd"
        return content.strip()




    def click(self,obj=None):
        if obj != None:
            obj.click()
        try:
            boo = self.timeout.until(
                EC.title_contains(("安全访问验证-拉勾网"))
            )
        except Exception as e:
            print(789)
            pass 
        else:
            # ################ 如果用requests 可以设这样设置 coolkies
            # 
            # img_url = self.driver.find_element(By.ID,"captcha").get_attribute("src")
            # cookies = self.driver.get_cookies()
            # print(cookies)
            # c = requests.cookies.RequestsCookieJar()

            # cookies={}
            # for cookie in self.driver.get_cookies():
            #     cookies[cookie['name']]=cookie['value']

            # with open("./captcha.png","wb") as f ,requests.session() as s:
            #     f.write(s.get(img_url,cookies = cookies).content)
            # self.verfiy(cookies,"./captcha.png")
            # # 截取验证码图片
            # #############################################################
            
            ################################## 截取验证码的方式
            if boo == True:
                while True:
                    try:
                        self.driver.save_screenshot('./captcha.png')
                        element = self.driver.find_element_by_xpath('//img[@id="captcha"]')    #找到验证码图片
                         # 打印元素大小
                        left = element.location['x']+207
                        top = element.location['y']+99
                        right = left + element.size['width']
                        bottom = top + element.size['height']
                        im = Image.open('./captcha.png')
                        im = im.crop((left,top, right, bottom))
                        im.save('./captcha.png')                       # 将得到的图片保存在本地
                        code = self.verfiy("./captcha.png")
                        input = self.timeout.until(
                            EC.presence_of_element_located((By.ID,"code"))
                        )
                        # input = self.driver.find_element(By.ID,"code")
                        input.clear()
                        input.send_keys(code)
                        submit = self.timeout.until(
                            EC.presence_of_element_located((By.ID,"submit"))
                        )
                        # submit = self.driver.find_element(By.ID,"submit")
                        time.sleep(3)
                        self.click(submit)
                        title = self.timeout.until(
                            EC.title_contains(("找工作-互联网招聘求职网-拉勾网"))
                        )
                        if title == True:
                            break

                        # if "https://passport.lagou.com/login" in self.driver.current_url:
                        #     print("登陆")
                        #     exit()
                        #     self.driver.quit()

                    except Exception as e:
                        # cookies = self.driver.get_cookies()
                        # cookies_dict = {}
                        # for cookie in cookies:
                        #     cookies_dict[cookies["name"]] = cookies["value"]
                        # jsonCookies = json.dumps(cookies_dict)
                        # with open('qqhomepage.json', 'w') as f:
                        #     f.write(jsonCookies)
                        break

                


    def index_page(self):
        self.driver.get(self.url)

        # 选择城市
        try:
            city_TAB = self.timeout.until(
                EC.presence_of_element_located((By.ID,"cboxContent")),
                EC.presence_of_element_located((By.ID,"search_input"))
            )
        except Exception as e:
            raise e
        else:
            # 获得城市的按钮并点击
            city_botton = city_TAB.find_element_by_partial_link_text(self.city)
            self.click(city_botton)
            # 获得收入狂
            text_input = self.driver.find_element(By.ID,"search_input")
            text_input.clear()
            text_input.send_keys(self.job)
            submit = self.driver.find_element(By.ID,"search_button")
            self.click(submit)

    def list_page(self):
        while True:
            html = etree.HTML(self.driver.page_source)
            urls = html.xpath("//div[@class = 'p_top']/a['position_link']/@href")
            self.parse_detail_page(urls)
            # 滚动底部
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # 获取下一页
            # next_paper = self.find_element(By.XPATH,"//div[@class ='pager_container']/span[last()]")
            try:
                next_paper = self.timeout.until(
                    EC.element_to_be_clickable((By.XPATH,"//div[@class ='pager_container']/span[last()]"))   
                )
                self.click(next_paper)
            except Exception as e:
                # self.driver.close()
                break
            time.sleep(2)

    def parse_detail_page(self,urls):
        print(4561)
        for url in urls:
           try:
                self.driver.execute_script('window.open("'+url+'");')
                self.driver.switch_to.window(self.driver.window_handles[1]) 
                html = etree.HTML(self.driver.page_source)
                data = {
                    "name": html.xpath("//span[@class = 'name']/text()")[0].strip(),
                    "gongzi":html.xpath("//dd[@class='job_request']/p[1]/span[1]/text()")[0].strip(),
                    "city":html.xpath("//dd[@class='job_request']/p[1]/span[2]/text()")[0].strip(),
                    "jingyan":html.xpath("//dd[@class='job_request']/p[1]/span[3]/text()")[0].strip(),
                    "xueli":html.xpath("//dd[@class='job_request']/p[1]/span[4]/text()")[0].strip(),
                    "leixing":html.xpath("//dd[@class='job_request']/p[1]/span[5]/text()")[0].strip()
                }
                print(data)
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                time.sleep(2)
           except Exception as e:
               break
               self.driver.quit()
               exit()


if __name__ == '__main__':
    lagou = LagouSpider()
    lagou("策划")
    lagou.start()

