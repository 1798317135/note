############################  描述器 #######################################
#
# 1.0 描述器其实就是 外界修改私有属性的接口
# 2.0 描述器 可以对属性的修改 进行过滤，等操作
# 3.0 描述器有三种 实现方式
# 4.0 我们通常都是使用实例 来调用描述器来进行操作，并不是通过类 来调用
# 5.0 描述器只有在 新式类里面才会生效，经典类不会生效
# 6.0 如果有的方法会覆盖描述器 描述器会失效 比如 __getattribute__会覆盖描述器的 __get__方法
# 7.0 描述器械分为两种 资料描述器 和 非资料描述器
#     --- 资料描述器是指 实现了 __get__ 和 __set__方法的描述器 
#     --- 非资料描述器是指 仅仅实现了 __get__ 方法
# 8.0 描述器的优先级 是 资料描述器 > 实例属性 > 非资料描述器
# 9.0 __set__
# 
# --- 方时一  通过property() 方法进行属性 和 操作属性，曾改 删  查 的方法的绑定
#     返回一个 绑定后的 属性 我们就可以直接操控这个 属性对私有属性进行 操作 
#     例子如下
class Persen:
    def __init__(self):
        self.__age = 18
    def setage(self,val):
        self.__age = val
    def getage(self):
        return self.__age
    def delage(self):
        del self.__age
    def __call__(self):
        print(1)
    age = property(getage,setage,delage,"""这是一个曾改删查age属性的方法""")

p = Persen()
print(p.age)
p.age = 19
del p.age
print(p.__dict__)

# --- 方式二 通过@property和 其他两个装饰器 来对操作私有属性属性的方法进行 装饰 获得 外界直接访问这个几个方法名
#      就可以调用这几个方法 来操作属性
class Dog:
    def __init__(self):
        self.__name = "bruce"
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,val):
        self.__name = val
    @name.deleter
    def name(self):
        del self.__name
d = Dog()
print(d.name)
d.name = "zhu"
del d.name
print(d.__dict__)

# --- 方式三 两种有一个问题 就是只能给单个私有属性 安装描述器
#      如果我们需要给多个私有属性添加描述器械 那么 如果如果 用上面的方法 
#      代码量太大且重复
#      所以我们可以使用把描述器 用__get__ ，__set__, __del__这些内置方法 
#      把描述器械封装到一个类里面
#      
#   --- 注意 
#      描述器 的实现原理是通过系统自动实现__getattribute__等等这个些内置方法让我们在外界
#     增加 查询 修改 删除 属性的时候自动关联到 描述器里面
#     如果 我们在类里面 自定义 这些内置方法 那么就会覆盖 系统定义的方法 那么描述器可能就不会生效
#     
#   --- 我们要把值储存在 instance 也就是实例身上 这样每个实例的储存的值 才不会共享
class Descriptor:
    def __get__(self,instance,woner):
        return instance.self
    def __set__(self,instance,value):
        instance.self = value
    def __delete__(self,instance):
        del instance.self
class Car:
    # def __init__(self):
    #     self.__color = Descriptor()
    color = Descriptor()
    # def __setattr__(self,key,val):
    #     print(key,val)
    # def __getattribute__(self,p):
    #     print(p)
    # def __delattr__(self,key):
    #     print(key)
    
c = Car()
c.color = "red"
c.he = 18
print(c.color)
c1 = Car()
c1.color = "black"
print(c1.color)
print(c.color)
print(c.__dict__)


