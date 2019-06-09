#############################  偏函数的概念  ##############################
#
#1.0 如果你偏爱 给某个函数的某个参数传递固定的值 那么我们可以用偏函数直接那个参数赋值 
#     而不需要重新赋值，称之为偏函数
#2.0 偏函数实际上是在不改变函数原体的前提上，函数外部重新设置函数某个参数的默认值 
#    从而达到重复使用，但是不需要重复设置相同参数的方法
#3.0 偏函数不会影响真函数在其他的地方的使用
#
# --- 自己设置偏函数
def myFun(arg1,arg2,arg3 = 5,arg4 = 6):
    print(arg1,arg2,arg3,arg4)

# 这个外面的函数就是偏函数,设置自己想要的默认值
# 
def pFun(new1,new2,new3 = 3,new4 = 4):
    myFun(new1,new2,new3,new4) #调用该函数

pFun(1,2) #1 2 3 4 输出的是自己设置的默认值

# --- functools.partial(func, *args, **keywords)
# 
import functools
newFun = functools.partial(myFun , arg3 = 13,arg4 = 11)
newFun(1,2)

################################### 偏函数的运用场景 ##################################
#
# 用int()来做事例
num = "1011001"
# int函数的第二个参数base 将几进制抓换为十进制 如果大量的把八进制转为为十进制 我们就可以设置偏爱函数
# 而不需要每次都设置成八进制
#
import functools

int2 = functools.partial(int,base = 16)
result1 = int2(num) 
print(result1,"1")

# 不会影响到其他int()的使用 
result = int(num)
print(result,"1")
