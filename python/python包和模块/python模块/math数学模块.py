# 先导入模块才可以使用
import math

# 天花板取整ceil()
num = 1.1
print(math.ceil(num))

# 地板取整floor()
num = 2.9
print(math.floor(num))

# 开平方sqrt()
print(math.sqrt(9))
print(math.sqrt(9)**2 == 9)

# log()算出 10的几次方是10000
print(math.log(10000,10))
print((10**math.log(10000,10))==10000)
print(math)