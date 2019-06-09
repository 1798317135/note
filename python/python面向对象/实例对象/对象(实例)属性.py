# 1.0 先定义一个人类
class Persen:
    pass

# 2.0 用人的类实例化出来一个对象
bruce = Persen()

#********************** 给对象添加属性（曾）  ***************************
# --- 如果赋值的这个对象不存在 那么就会新增这个属性并赋值
#     如果这个对象已经存在那么 就会覆盖这个对象属性原来的值
#     
bruce.age = 18
bruce.height = 180

# ********************* 查看对象的属性 和 属性值 （查）***************
# 
# ---__dict__方法可以查看对象里面的所有属性 
#   返回一个字典类型 
#   key就是对象的属性名称
#   val 就是对象属性的值
#   
print(bruce.__dict__)

# --- 用obj.attr的方式访问对象属性
#     如果访问的是一个对象不存在的属性
#     报错AttributeError: 'Persen' object has no attribute 'wight'
print(bruce.age)
# print(bruce.wight)
# 
# 
#*********************** 修改对象的属性值（改） ***********************
#
# --- 如果访问的对象属性存在，那么从新赋值就可以覆盖原来的值
#     如果值是可变的类型，只是修改这个可变值的本身，那么不会覆盖原来的值，而是修改原来的值 
#     
bruce.age = 20
bruce.arr = [1,2,3,4]
bruce.arr.append("aa")
print(bruce.__dict__)

# *********************** 删除对象的属性 **************************
# 
# --- del 语句可以删除对象的属性
print(bruce.__dict__)
del bruce.age
print(bruce.__dict__)
# print(bruce.age)



#************************** 对象属性的注意点 ***********************
#
# --- 同一个类构造出的不同的对象 都是一个独立的个体 每一个对象的属性不并不互通
p1 = Persen()
p2 = Persen()

print(p1 == p2)

# 但是他们来自同一个类
print(p1.__class__ ==  p2.__class__)

p1.age = 18
p2.address = "上海"

# 他们的属性是私有的
# print(p1.address,p2.age)

# ************************** 对象属性的访问流程 *********************
# 
# --- 我们可以通过对象去查找构造他的类里面的属性
#     基本的查找路线是现在对象里面找，如果没有则会到他__class__ 指向的类里面去查找
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


# ************************** 对象属性的储存问题  *********************
# 
# --- 对象的所有属性都储存在 这个对象的 __dict__方法里面__dict__是一个字典类型的数据 
#     可以读 也可以修改
class Car:
    pass
mpv = Car()
print(mpv.__dict__)
mpv.__dict__ = {"color":"red"}
mpv.width = 18
mpv.height = 19
mpv.__dict__["color"] = "black"
print(mpv.color)
print(mpv.__dict__)