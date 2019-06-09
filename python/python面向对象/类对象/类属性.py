# ##############################  万物皆对象 类本身也是一个对象 ##########################
# 
class Persen:
    pass
    # __name__ = "Persen"

# --- 1.0 每一个类都有一个属性 __name__ = Classname
#     ClassName 就是类名
#     类名的本质就是一个变量指向这个类本身
#     所以类名也是一个变量
#     
p1 = Persen
print(p1)
# 
# **************************** 新增类增加属性是（曾） **********************
# ------ 方式一
# 
# --- 把类当作对象增加属性，那么方式和对象一样
# 
Persen.age = 18
print(Persen.__dict__)
# 
# ------- 方式二
# 
# --- 在类里面直接添加 属性
#     这个给类添加属性的方法 是比较常用的
class Dog:
    age = 18
    name = "小黑"
print(Dog.age)
print(Dog.name)
print(Dog.__dict__)

# **************************** 查看类属性是（查） **********************
# 
# __class__ 对象属性去修改这个对象指向的类
# 
# ----------- 1.0 我们可以通过对象去查找构造他的类里面的属性
#               基本的查找路线是，先在对象里面找，如果没有则会到他__class__ 指向的类里面去查找
#     
Persen.age = 18
p3 = Persen()

# p3这个对象里面并没有age这个属性，访问的时候他 会先自己的里面找 如果没有找到就会到他指向的类里面找
# 类里面有Persen.age = 18 所以这个对象也可以访问到
print(p3.age)


# --- 我们可以通过__class__ 对象属性去修改这个对象指向的类

class Dog:
    height = 12
# 这个对象现在指向的是 Persen类 所有他可以访问 Persen类的属性
print(p3.__class__)

# 那么p3对象的指针指向Dog 那么他就访问不了这个Persen类里面的属性了，
# 但是可以访问他现在指向的那个Dog类
p3.__class__ = Dog
# print(p3.age)
print(p3.height)

# --- 我们可以通过class.classAttr 方法查看类的属性
print(Persen.age)

# **************************** 对象属性是（改） **********************
# 
# 通过CassName.attr = val 如果这个类属性存在则会覆盖原来的值
# 如果不存在 则会新增这个类属性
# 如果这个属性是可变的 那么就该这个类属性的值 不会覆盖以前的 而是会改变这个值
# 注意--- 对象只能查看类里面的属性 但是不可以就该类的属性
Persen.age = 418
Persen.arr = [1,2,3,4]
print(Persen.arr)
Persen.arr.append("aa")
print(Persen.arr)
print(Persen.age) 

# **************************** 删除类的属性（删除） ********************
# 
# --- del 语句可以删除类里面的属性  对象删除的只是对象内部的属性 不是类里面的属性
p1 = Persen()
print(Persen.age)
print(p1.age)
del Persen.age
# del p1.age
# print(Persen.age)
# print(p1.age)

# ****************************** 注意点 ********************************
# 
# ------------- 类属性的存储问题
# --- 类的所有属性 都储存在 类里面的 __dict__ 字典里面
#     类的__dict__ 和对象的__dict__属性的区别就是，
#     类的是只读的，不能直接修改的和写入

class Car:
    window = "purple"
Car.color = "red"
Car.widht = "418"
print(Car.__dict__)
# Car.__dict__ = {"widht":18,"height":50}
# 
# ------------- 类属性的共享文体
# 
# ---每个类实例化的对象将共享这个类里面的属性
#    当类里面的值发生改变的时候，他实例化出来的所有对象调用的这个属性的值跟着发生改变

crv = Car()
crv.window = "orange"
mpv = Car()
a3 = Car()
print(crv.window,mpv.window,a3.window)

# --------------- 限制对象属性
#
# ---class.__slots__方法可以限制此类实例化的对象 添加属性
# 
#     他会导致类的__dict__方法失灵
#    规定从这个类实例化的对象 可以添加的属性
#    如果对象添加了限制之外的属性则会报错
#    以列表的方式进行添加无限制的对象属性
class Phone:
    pass
    __slots__ = ["aEe"]
print(Phone.__name__)
ipone = Phone()
ipone.aEe = 4
# print(ipone.__dict__)
 