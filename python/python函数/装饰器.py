
################################### 装饰器 ##################################
#
#************** 装饰器的作用是在函数名 和 函数体不变的前提下给一个函数增加额外的代码
#
#
# --- 1.0 装饰器直接会被调用 
def dd(fun):
    print("999") #只要被装饰 等于直接调用装饰器函数 打印999
    def inner():
        print("-------")
        fun()
    return inner
@dd
def cc():
    print("aaaa")

cc()

# --- 场景
# 在发说说和发图片之前增加登录验证，并且不改变函数
# -- @checkLogin
# 这个闭包就是一个装饰器
# 

def checkLogin(fun):
    def inner():
        login()
        fun()
    return inner


# -- 1.0 功能函数
def login():
    print("登录验证")

@checkLogin
def fss():
    print("发说说")

# fss = checkLogin(fss)
@checkLogin
def ftp():
    print("发图片")
# ftp = checkLogin(ftp)

# -- 2.0 业务逻辑
btnIndex = 0
if btnIndex == 1:
    fss()
else:
    ftp()

# ****************************** 装饰器的叠加 ************************************
# 
# 从上而下的装饰
# 从下而上的执行
# 
def decorator1(fun):
    def inner():
        print("----------------")
        fun()
    return inner
def decorator2(fun):
    def inner():
        print("****************")
        fun()
    return inner


@decorator1 #fun = decorator1(fun)
# print("----------------")
# print("****************")
# print("阿萨德发射点发")
@decorator2 #fun = decorator2(fun)
# print("****************")
# print("阿萨德发射点发")
def fun():
    print("阿萨德发射点发")

fun()


##################################  装饰带有参数和返回值的函数 #################################
#
#1.0 装饰带有参数和返回值的函数，关键是给装饰器的闭包增加形参，
#   并且给形参装包 然后解包到被调用的函数的形参当中
# 2.0 关键是保证装饰器的格式 和 被装饰函数的格式一样
# 
# 3.0 返回 被调用函数 就可以得到函数返回的值
# 
def deco(fun):
    def inner(*args,**kwarg):
        print("-" * 30)
        # print(args,kwarg)
        result = fun(*args,**kwarg)
        # 当函数有返回值的话会返回函数的返回值 如果没有就是none
        return result
    return inner
@deco
def heh(num,num1,num2):
    print(num + num1 +num2)
heh(1,2,3)

################################# 给装饰器增加参数 #####################################
#
# 1.0给装饰器外层，多嵌套一个曾函数 用来生成内层装饰器的参数
# 2.0 先计算@后面的内容，然后把这个内容当作装饰起
# 3.0 装饰器的格式是固定的，所以不可以直接给装饰器传递多余的参数
#       那么可以通过参数函数 传递给装饰器 然后把装饰器返回出来 就可以用了
def getArgs(**aa):
    def dec(fun):
        def inner(*args,**kwargs):
            print(aa["symbol"] * aa["width"])   # 想自定义这里的参数 不能在装饰器里面修改
                                                #可以通过在外面嵌套一层函数来传递参数，
                                                #并把装饰器返回出去
            result = fun(*args,**kwargs)
            return result
        return inner
    return dec

@getArgs(symbol ="o",width = 30)
def test(num,num1,name="yang"):
    return num + num1,name
result = test(1, 3,name="zhu")

# 用装饰器在前面添加一段*号
print(result)
    



# ######################################  系统自带的装饰器 ######################################
class Persen:
    @classmethod
    def cls(cls):
        print("@classmethod 这样装饰一个类方法",cls)
    @staticmethod
    def sta():
        print("@staticmethod装饰一个静态方法",)
# @classmathed 可以在 类里面装饰一个类方法 
Persen.cls()
# @staticmethod 可以在类里装饰一个静态方法
Persen.sta()

# @property 装饰器可以给 装饰 类私有属性的操作方法 从而可以在外面直接调用这个些装饰过的 方法名来进行操作
# 私有化方法
class Dog:
    def __init__(self):
        self.__name = "zhu"
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value           
    @name.deleter
    def name(self):
        del self.__name
d = Dog()
d.name = "burce"
print(d.name)
del d.name

# @functools.total_ordering 装饰的类 比较调用的方法是 可以叠加比较
#  也就是说可以叠加 大于 和 等于 或者其他的
import functools
@functools.total_ordering
class Da:
    def __init__(self,age):
        self.ages = age
    def __eq__(self,other):
        return self.ages == other.ages
    def __gt__(self,other):
        return self.ages > other.ages
d = Da(19)
d1 = Da(19)
print(d >= d1)

############################################  类装饰器 ##############################
#
# --- 上面实现的装饰器是用函数实现的 
# --- 我们也可以通过类 来实现装饰器
# --- 类装饰器 和 函数 装饰器 原理上一样 
#     我们可以根据装饰器的特性 在类里面找相应的方法 来实现装饰器

class dec:
    def __init__(self,fun):
        self.funs = fun
    def __call__(self):
        print("111111")
        self.funs()

@dec # fa = dec(fa)
def fa():
    print("发微博")

fa()
    
