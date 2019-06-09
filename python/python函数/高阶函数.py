

########################### 高阶函数 ##################################
#
#1.0 高阶函数指的是 函数的形参内可以调用另外一个函数体 称之为高阶函数
#   函数体指的是函数本身的代码
# 
# --- 函数名本身就是一个变量 形参也是变量 
#   相当于把函数名 指针指向函数体空间 
#   
def myfun(a,b):
    print(a + b)

print(myfun)
print(id(myfun))

# --- 函数本身也可以作为数据传递给另外一个变量
test = myfun
test(1,2)

# --- sorted()就是高阶函数 因为他的形参里可以调用另外一个函数体
# 
arr = [{"age":18},{"age":17},{"age":16},{"age":20}]
def test(x):
    return x["age"]

result = sorted(arr,key = test,reverse = False)
print(result)


# --- 自定义高阶函数
# 
def math1(a,b,mfun):
    print(mfun(a,b))

def jia(a,b):
    return a + b
def jian(a,b):
    return a - b

math1(3,2,jian)