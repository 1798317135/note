import hashlib


######################## md5加密
# 1.0 创建一个MD5对象
m = hashlib.md5()

# 2.0 更新一个需要机密的字符串
m.update("abc".encode("utf-8")) # 注意转码
# m.update("hollow word".encode("utf-8"))

# 3.0 打印机密后的结果
dig = m.digest() #二进制
he = m.hexdigest() #十六进制
print(dig,he)

sha1 = hashlib.sha1()
sha1.update("string".encode('utf-8'))
res = sha1.hexdigest()
print("sha1加密结果:",res)

# ######## sha256 ########

sha256 = hashlib.sha256()
sha256.update("string".encode('utf-8'))
res = sha256.hexdigest()
print("sha256加密结果:",res)


# ######## sha384 ########

sha384 = hashlib.sha384()
sha384.update("string".encode('utf-8'))
res = sha384.hexdigest()
print("sha384加密结果:",res)

# ######## sha512 ########

sha512= hashlib.sha512()
sha512.update("string".encode('utf-8'))
res = sha512.hexdigest()
print("sha512加密结果:",res)


######################## 高级加密
#
# --- 普通加密
# 
low = hashlib.md5()
low.update("你好".encode("utf-8"))
result = low.hexdigest()
print(result)

# --- 高级加密
low = hashlib.md5(b"abc")
low.update("123456".encode("utf-8"))
res = low.hexdigest()
print(res)
