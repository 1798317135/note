import json
import pickle
###################################### 序列化简介
#
# 在程序得运行中所有变量都储存到内存中，当程序结束，变量就会销毁
# 所以序列化 就是将内存中得数据保存到磁盘当中或者传输保存到其他地方，
# 这中数据得保存和传输得过程称为序列化
# 
# 反序列化 就是将序列化对象得数据重新读写到内存，这个过程称为反序列化
# 
# 
# #################################### 序列化得分类
# python有两种序列化模块
# pickle 和 json
# pickle 可以将数据以二级字节保存到本地，但是他序列化得对象 ，只能还是让他自己使用，不同版本得python可能不兼容 这些 序列化数据
# 如果想要共享得话 json是标准得序列化 他将序列化对象以 json格式保存，所有json可以在其他语言中共享
# 
# json 是文本序列化格式默认是utf-8 pickle是二进制序列化格式
# 
# ################################### pickle 
# 
# pickle模块有四种方法
# jump()、和 jumps() 序列化 load() 和 loads() 反序列化
# 
# --- jumps(obj)将 python 对象序列化成二进制数据
#     obj 表示一个打开得文件对象，
obj = {"name":"李小龙","age":18}
result = pickle.dumps(obj)
print(result)

# --- jumps(obj,file) 直接将序列化的二进制数据保存到文件
with open("obj.txt","wb") as f:
    pickle.dump(obj,f)

# --- loads() 将二进制得数据反序列化成python对象
obj = pickle.loads(result)
print(obj,type(obj))

# --- load() 将一个序列化的文件反序列化
with open("obj.txt","rb") as f:
    obj = pickle.load(f)
    print(obj,type(obj))
    
# print(obj)
# 他提提供了四种方法
# 两种序列化方法dump 和 dumps
# 两种反序列化方法 load 和 loads
# 
# --- json.dumps  将 Python 对象编码成 JSON 字符串
# json.dumps(,obj, skipkeys, ensure_ascii, check_circular, allow_nan, cls, indent, separators, encoding, default, **kw)

# # --- obj为python对象 indent 可以控制序列化后的缩进格式化收出

# obj = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 , "年后":"辣豆腐4"} ]
# result  = json.dumps(obj,indent=2)
# print(result)
# print(type(result))

# # --- json.dump 将python对象源码成str后保存在文件当中
# #     nsure_ascii=False 可以让汉字总被转换成unicode码
# #     
# with open("dump.json","w",encoding = 'utf-8') as f:
#     json.dump(obj,f,indent=3,ensure_ascii=False)

# # --- json.loads  将已编码的 JSON 字符串解码为 Python 对象
# result = json.loads(result)
# print(result)
# print(type(result))

# # --- json.load 将已编码的文件转换为python对象
# with open("dump.json","r",encoding="utf-8") as f:
#     obj = json.load(f)

# print(obj)
# print(type(obj))


############################# 