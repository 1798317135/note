# ########################### 浅拷贝 copy()
# 1.0 浅拷贝只复制对象的引用，并没有拷贝这个对象，
# 
# 2.0 直接赋值操作默认的就是浅拷贝
#     当原始列表发生改变的时候，被赋值的变量的值也会发生改变
#     
# 3.0 copy浅拷贝，没有拷贝子对象，所以原始数据改变，子对象会改变
# 
# 4.0 copy 浅拷贝只拷贝列表的第一层，重新开辟一块内存，把赋值的第一层内容拷贝进去
#     当原始数据第一层发生改变的时候，并不会影响到新拷贝的一层
#     但是嵌套的子对象，并没有被拷贝，仍然引用这公共的地址
#     当子对象发生改变的时候，应用他地址的对象都发生改变
#     
# a = [1,2,3,4,5]
# a.append(["aa","bb"])
# b = a
# print(b)
# print(a)
# print(b)

from copy import copy,deepcopy
# a = [1,2,3,4,["aa","bb"]]
# b = copy(a)
# print(a)
# print(b)
# a.append(5)
# a[4].append("cc")
# print(a)
# print(b)
# print(id(a))
# print(id(b))
# print(a[4])
# print(id(a[4]))
# print(id(b[4]))
# a[4].append("cc")
# print(a)
# print(b)
################# 深拷贝deepcopy
#
#1.0 深拷贝把对象的全部内容拷贝下来重新开辟空间存放,当原始内容发生改变并不会影响到这块内容
# a = [1,2,3,["aa","bb","cc"]]
# b  = deepcopy(a)
# print(a,id(a))
# print(b,id(b))
# print(a[3],id(a[3]))
# print(b[3],id(b[3]))
# a.append(4)
# print(a)
# print(b)
# a[3].append("cc")
# print(a)
# print(b)