# 1.0 super()本身也是一个类，
# 2.0 super()只在新式类里面有效，在经典类无效
# 3.0 super()起着代理作用 代理指定的类，执行MRO链条的下一级节点 ，不是一定是父类
#     那么出现三个问题
#     --- 1.0 沿着谁的MRO链条
#     --- 2.0 执行谁的下一级节点
#     --- 3.0 如何如何应对类方法，实例方法，和静态方法的参数传递问题
# 4.0 super语法原理 super(type,obj) 第一个是指定 执行 谁的 下一级节点
#     第二个参数，执行给方法 传递的参数 如果调用的是 实例方法 就穿实例 如果是 类就传类
#     def super(type,obj):
#     mro = inst_class_.mro()
#     return mor(mor.index(cls) + 1)
# 5.0 python 3.0 x 版本 直接 可以不传递参数
#      系统会自动的查找super()所在的类 和传递的参数
# class D:
#     def __init__(self):
#         self.dd = 4
#         print("d")

# class C(D):
#     def __init__(self):
#         self.cc = 3
#         super().__init__()
#         print("c")
# # class B(D):
# #     def __init__(self):
# #         self.bb = 2
# #         super().__init__()
# #         print("b") 
# class A(C):
#     def __init__(self):
#         self.aa = 1
#         super().__init__()
#         print("a")

# a = A()
# # print(a.dd)
# print(A.mro())
# class B:

#     def __new__(cls):
#         return object.__new__(cls)

#     def __init__(self):
#         self.age = 18
#         print(self,"B_init")

# class A(B):

#     def __new__(cls):
#         print(cls,"A_new")
#         return "aa"

#     def __init__(self):
#         # super().__init__()
#         print(self,"A_init")

# a = A()
# print(a.age)
# b = B()
# print(b.age)
# -*- coding: utf-8 -*-



