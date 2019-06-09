
####################################  闭包的定义 ###################################
#
# 1.0 闭包和javascript里面的闭包略有不同之处
# 
# 2.0 闭包是指内部函数用到了外部函数的变量 这样就形成了一个闭包，并且
# 外部函数把内部函数体返回出去 那么返回出去这个函数体和他引用外部函数的变量统称为闭包
# 
def aa():
    num = 0
    def bb():
        num1 = num + 1
    return bb

# --- 闭包可以根据外层函数的配置信息生成不同作用功能的函数

def createLine(content,width,flag):
    str = "%s" %(content)
    def line1():
        print(str.center(len(str) + width,flag))

    return line1

result = createLine("asdf", 20,"*")
result()
result = createLine("123", 10,"/")
result()
result = createLine("adf", 5,"-")
result()

#############################  注意事项 #####################################
#
#
# --- nonlocal修改闭包引用的外部变量，更改为全局变量
#       如果不使用则会识别成闭包内部重新声明的变量
# 
def fun():
    aa = 1
    def fun1():
        nonlocal aa
        aa = 3
        print(aa)
    print(aa)
    fun1()
    print(aa)
    return fun1
fun()

# --- 函数在没有调用之前 里面的变量都还是标识，并没有明确的值
# --- 当函数被调用时，才会给函数体内部的变量赋值 也就是说函数体内部的变量在被调用的那行代码处开始赋值

def fun3():
    aa = 3
    def fun4():
        print(aa)
    aa = 6
    # 返回出去的时候才被赋值为6 之前只是标识并没有赋值
    return fun4
result = fun3()
result()

# --- 和javascript闭包类似 处理循环体内异步问题 ，不能同步取出外层循环每次循环同步赋值的问题 

# def test():
#     arr = []
#     for x in range(0,6):
#         def test1():
#             print(x)
#         arr.append(test1)
#     return arr
# result = test()
# # 每个函数打印的都是5 因为上面循环的时候没有赋值 现在调用才回去找x x循环完毕就是5
# # 所以都是五
# 
# result[0]() 
# result[1]()
# result[2]()

# ---- 闭包循环内部，闭包解决同步赋值问题
def test():
    arr = []
    for x in range(0,6):
        def test1(num):
            def inner():
                print(num)
            return inner
        arr.append(test1(x))
    return arr
result = test()
result[0]()
result[1]()
result[2]()
result[3]()
result[4]()
result[5]()
# 
####################################### 闭包自增函数 #####################################
#
def add(num):
    """
    自增函数每次调用自增一
    """
    def test():
        nonlocal num
        num += 1
        return num
    return test
result = add(0)
# 每次调用自增一
print(result())
print(result())
print(result())    
