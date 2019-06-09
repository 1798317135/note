# 1.0 requests 模块可以用各种类型发送http请求
# 2.0 requests 模块可以获取请求后返回的数据对象
# 
################################ 安装  #####################################
#
# pip install requests
# 或者在虚拟环境下 安装
# pipevn install requests
# 
import requests
# ############################# 发送请求 ###################################
# --- get方式
#     1.0 状态码 200 说明请求成功
#     2.0 params 参数可以给 get请求 添加参数，以字典的格式传参
#         也可以给一个key 传递一个列表值,可以达到给一个key 传递多个值

arg = {
    'key1':'value1',
    'key2':'value2',
    'key3':['value1','value2'],
}
# r = requests.get('http://www.runoob.com/python3/python-mongodb.html',params = arg)
# --- url 方法可以查看具体url地址
# print(r.url)

# --- post方式
#     data 参数可以给post 请求设置参数
#     
r = requests.post('http://www.runoob.com/python3/python-mongodb.html',data = {'key':'value'})
print(r.url)

########################################  相应内容 ##################################
#
# --- text方法可以查看响应的内容
# print(r.text[0:100])

# ---r.encoding 可以查看和改正 响应的编码
# print(r.encoding) 
# r.encoding = 'utf-8'

