
# 匿名函数 lambad 函数 与 javascript的匿名函数有很大差别
# 匿名函数 不宜处理复杂的程序
# 
# ****** 方式一 ********* 
#  --- (lambad 形参:返回值)(实参)
result = (lambda a,b:a + b)(1,2)
print(result)

# ******* 方式二 ********
# 
# --- 用变量接收 匿名函数体 lambad 形参:返回值
result = lambda a,b : a -b
print(result(5, 1))


# ******* 运用场景 ********
# 
# --- sorted() 里面的key接收的函数体可以用匿名函数 ，非常方便
arr = [{"name":"c","age":15},{"name":"a","age":16},{"name":"b","age":17}]

result = sorted(arr,key = lambda x : x["name"],reverse = True)
print(result)