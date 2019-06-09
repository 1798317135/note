#urllib是一个包含几个模块来处理请求的库。分别是：

# 1.0 urllib.request 发送http请求

# 2.0 urllib.error 处理请求过程中,出现的异常。

# 3.0 urllib.parse 解析url

# 4.0 urllib.robotparser 解析robots.txt 文件

################# urllib.request
# request当中使用最多的模块,涉及请求，响应，浏览器模拟，代理，cookie等功能。
from urllib import request
from urllib.request import Request
from urllib import parse
import http.cookiejar
# ******** urlopen
# 
# url:  需要打开的网址
# data：Post提交的数据
# timeout：设置网站的访问超时时间

# response = request.urlopen(url = 'http://www.baihe.com')
# f = open("baidu.html","w",encoding = 'utf-8')
# f.write(response.read().decode('utf-8'))
# print(response.info())
# print(response.getcode())
# print(response.geturl())
# --- read 返回文本数据
# --- info 服务器返回的头信息
# --- getcode 状态码
# --- geturl 请求的url
# 
# ******** 添加header 头部信息
# 
# urlopen 不支持直接添加头部信息
# 需要Request创建一个请求信息对象 然后把他传递给urlopen
# url = 'http://www.baidu.com'
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
# }
# rt = Request(url,headers = headers)
# respons = request.urlopen(rt)
# print(rt.get_method()) #判断请求方法

# ********** cookie 得使用
# # 1.0 创建coopkieJar 对象
# cookie = http.cookiejar.CookieJar()

# # 2.0 使用HTTPCookieProcessor创建cookie处理器
# handler = request.HTTPCookieProcessor(cookie)

# # 3.0 勾践opener 对象
# opener = request.build_opener(handler)

# respons = opener.open('http://httpbin.org/cookie/set?course=abc')

# ********* 快速下载urlretrieve
# request.urlretrieve('http://bpic.588ku.com/element_origin_min_pic/19/03/06/56b5719267a99adf5045edc5b144b93e.jpg','baidu.jpg')

#### 也可以将cookie 信息保存到本地
# cookiejar = http.cookiejar.MozillaCookieJar('cookie.txt')
# handler = request.HTTPCookieProcessor(cookiejar)
# opener = request.build_opener(handler)
# respons = opener.open('http://httpbin.org/cookies/set?course=abc')
# cookiejar.save(ignore_discard=True)

#### 读取本地cookie
# cookiejar = http.cookiejar.MozillaCookieJar('cookie.txt')
# cookiejar.load(ignore_discard = True)
# handler = request.HTTPCookieProcessor(cookiejar)
# opener = request.build_opener(handler)
# # respons = opener.open('http://httpbin.org/cookies/set?course=132')
# for cookie in cookiejar:
#     print(cookie)
#
#
#### 设置代理
# url = 'http://httpbin.org/ip'
# proxy = {'http':'39.137.46.73:8080'}
# proxies = request.ProxyHandler(proxy) # 创建代理处理器
# opener = request.build_opener(proxies,request.HTTPHandler) # 创建特定的opener对象
# request.install_opener(opener) # 安装全局的opener 把urlopen也变成特定的opener
# data = request.urlopen(url)
# print(data.read().decode())
# #
####################### urllib.parse
# --- urllib.parse.urljoin 拼接url
#基于一个base URL和另一个URL构造一个绝对URL,url必须为一致站点,
#否则后面参数会覆盖前面的host
print(parse.urljoin('https://www.jianshu.com/xyz','123.html'))

# --- urllib.parse.urlencode 字典转字符串
dic = {
    'key1':'value',
    'key2':'value'
}
result = parse.urlencode(dic)
print(result)
# --- urllib.parse.parse_qs() 将url参数转换为 字典
result = parse.parse_qs(result)
print(result)

# --- urllib.parse.quote url编码
print(parse.quote('河南',encoding = 'utf-8'))
aa = parse.quote('河南',encoding = 'utf-8')
# --- urllib.parse.unquote url解码
print(parse.unquote(aa))

# --- urllib.parse.urlsplie 拆分url
url = 'https://passport.baidu.com/v2/v3/;45index.html?sd#1'
print(parse.urlsplit(url))

