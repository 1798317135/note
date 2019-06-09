import requests

# #############################  发送请求 得到一个response对象 ##############################
# 
# r = requests.get("https://api.github.com/events")
# r = requests.post("'http://httpbin.org/post",data = {"key:value"})
# r = requests.put('http://httpbin.org/put', data = {'key':'value'})
# r = requests.delete('http://httpbin.org/delete')
# r = requests.head('http://httpbin.org/get')
# r = requests.options('http://httpbin.org/get')
# x
# #############################  #传递参数、  ###############################################
# --- 参数都是字典类型的数据
dict = {
    'key1':'value1',
    'key2':'value2',
}

# --- params 关键字给get请求传递参数
url = 'http://www.baidu.com'

# --- headers 关键字 设置请头 
#     请求头是一个字典类型或者json类型的数据
#     请求头内部可以包含cookies 请求类型等信息 
#     可以用浏览器的开发者工具查看
headers = {
    'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',

}

# --- allow_redirects 禁止重定向 
r = requests.get(url,params = dict,headers = headers,timeout = 2,allow_redirects = False)


# --- data关键字
#     给post 请求添加参数
#     可以使用元祖的方式给一个键 传递多个值
data = (('key2','value2'),('key2','value3'))

# --- json 关键字
#     可以给传入的字典转换为json格式
#
# 
# --- file 关键字

#    上传文件
files = {
    'file':open('cookies.py','r')
}  

# --- timeout 关键字 设置超时
# 
r = requests.post(url,data = data,json = data,files = files,timeout = 2,allow_redirects = True)
print(r)


# ############################# 响应内容 ###################################################
# 
# --- response.headers响应头
#     返回一个字典对大小写不敏感
print(r.headers)
print(r.headers['content-length'])

# --- response.url 获取访问的url 
print(r.url)

# --- response.text 获得响应的内容
# print(r.text)
# 
# --- response.encoding 获取或者设置响应的字符类型 修改的话需要在获取内容之前修改
print(r.encoding)
# r.encoding = 'utf-8'
# print(r.text)

# --- response.content 获取响应的二级制数据
#      如果text 不能自动识别字符类型，就需要用到
#      response.content.encode('utf-8')来手动解码
# print(r.content)
# 
# --- response.status_code 获取响应状态码
#     requests.codes 自带状态码对象 用来判断状态 
#     requests.codes.ok
# print(requests.codes.__dict__)
print(r.status_code == requests.codes.not_found)

# ---r.raise_for_status() 如果发生异常 可以用这个抛出请求
print(r.raise_for_status())

# --- response.cookies 获取返回的cookie信息
print(r.cookies)

# --- response.cookeies.get_dict()可以获取字典形式得cookie信息
print(r.cookies.get_dict())
# 
# --- json 响应内容 
#     自带的json解析器
print(r.json())

#############################代理
# 代理可以委托其他ip来访问目标网站
# 通常需要网上购买
# 或者自己爬取一个代理ip池
response = requests.get('http://www.httpbin.org/ip',proxies={'http':"127.0.0.1:1200"})



#############################  绘画
# 我们为了保存cookie需要开启一次会话
session = requests.Session()
session.get(url,params=params)

########################### 处理不信任得https
# 如果在请求https 颁发得证书是不正规得 需要手动得设置verify=false
r = requests.get(url,verify = False)

################################# 重定向与请求历史 ########################
#
# --- 默认情况下，除了 HEAD请求 Requests 会自动处理所有重定向。
# --- history 追踪重定向信息
# --- allow_redirects 除了head()请求 之外的任何请求方式都可以用 这个来禁用重定向 值为false禁用 true 开启
print(r.history)

################################ 错误与异常 ##########################
#
#--- 遇到网络问题（如：DNS 查询失败、拒绝连接等）时，Requests 会抛出一个 ConnectionError 异常。
