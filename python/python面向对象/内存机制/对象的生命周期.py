########################################  对象的生命周期 ###################################
#
# 1.0 对象的生命周期是指，对象从创建 到 释放的过程
# 2.0 我们可以通过 几个内置方法 来监听和改变 对象从创建到销毁的过程
# 
# class Persen:
# # --- __new__ 这个方法可以监听对象的创建 也就是在创建的实例的时候会自动调用这个方法
#     def __new__(cls):
#         print("你创建的对象被拦截了")
#     def __init__(self):
#         print
# # --- __del__这个方法可以释放对象
#     def __del__(self):
#         print("这个对象被释放了")
# p = Persen()

#

# ------------ 每次创建一个实例，曾一 释放一个实例 减一
class Dog:
    __count = 0
    def __init__(self):
        Dog.__count+=1      
    def __del__(self):
        Dog.__count-=1
    @classmethod
    def log(cls):
        print("现在创建了%d个实例" % cls.__count)
d = Dog()
d1 = Dog()
d3 = Dog()
# del d1
d.log()