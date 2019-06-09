
# 只读属性顾名思义就是只能读 不能写入的实例属性

# 设置只读属性的方法有很多种因为python的私有属性是伪私有。一般使用最有一种__setAttr__内置方法
# 1.0 把属性私有化，通过创建获取的方法 ，公开部分私有化
#      这样有几个缺点。
#      第一：必须调用这个方法才可以查看
#      第二：用这个方法更改私有化的值，虽然没有真正的更改，
#      但是，却不会报错，给人一种已经更改的假象
#      那么我们可以用@property 这个装饰器 弥补这些缺点
#      
# 2.0 用property()函数 可以给私有属性绑定，读，改，删 方法 只绑定读，就可以达到绑定的目的
#      但是任然不是很安全，因为外界还可以通过 名字重整的机制 访问和修改到这个私有属性
# 3.0 @property 装饰器 和上边方法类似 但是更加方便，@property装饰读方法，@方法名字.setter 装饰写
#      @deleter 装饰删除方法
# 4.0 用__setattr__内置方法，只要类，涉及到 obj.attr = val 这种修改 或者 设置属性值的语句 都会通过__setattr__
#     所有运用这个方法的特性 可以过滤指定，外界对属性值的操作
# 
#  |    --- 1.0 定义一个继承objcet 的新式类
#  |    
#  |   class property(object)
#  |   
#  |   --- 2.0 property()函数有四个形参
#  |    
#  |  property(fget=None, fset=None, fdel=None, doc=None)
#  |
#  |  Property attribute.
#  |
#  |    fget
#  |      function to be used for getting an attribute value
#          --- fget是用于获取属性值的函数
#  |    fset
#  |      function to be used for setting an attribute value
#         --- fset是用于设置属性值的函数
#  |    fdel
#  |      function to be used for del'ing an attribute
#         --- fdel是用于删除属性值的函数
#  |    doc
#  |      docstring
#         doc 添加项目文本
#  |
#  |  Typical use is to define a managed attribute x:
#      --- 典型的用法是定义一个托管的私有属性 x
#      
#  |   ********************  property()实现方法 *****************************
#  
#  |  class C(object):
#         --- 这是类里面获取 x 属性的实例方法 可以把这个方法设置到 property(fget形参)
#  |      def getx(self): return self._x
#          --- 这是类里面设置 x 属性的实例方法 可以把这个方法设置到 property(fset形参)
#  |      def setx(self, value): self._x = value
#  
#          --- 这个是删除 x 属性的方法 赋值给property(fdel)
#  |      def delx(self): del self._x
#          --- 把设置好的property()函数 传给 x 变量
#  |      x = property(getx, setx, delx, "I'm the 'x' property.")
#  |
#  |  Decorators make defining new properties or modifying existing ones easy:
#  |   ---装饰器使定义新属性或修改现有属性变得容易
#  
#  |  class C(object):
#  |      @property
#  |      def x(self):
#  |          "I am the 'x' property."
#  |          return self._x
#  |      @x.setter
#  |      def x(self, value):
#  |          self._x = value
#  |      @x.deleter
#  |      def x(self):
#  |          del self._x
#  |
#  |  Methods defined here:
#  |
#  |  __delete__(self, instance, /)
#  |      Delete an attribute of instance.
#  |
#  |  __get__(self, instance, owner, /)
#  |      Return an attribute of instance, which is of type owner.
#  |
#  |  __getattribute__(self, name, /)
#  |      Return getattr(self, name).
#  |
#  |  __init__(self, /, *args, **kwargs)
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |
#  |  __set__(self, instance, value, /)
#  |      Set an attribute of instance to value.
#  |
#  |  deleter(...)
#  |      Descriptor to change the deleter on a property.
#  |
#  |  getter(...)
#  |      Descriptor to change the getter on a property.
#  |
#  |  setter(...)
#  |      Descriptor to change the setter on a property.
#  |
#  |  ----------------------------------------------------------------------
#  |  Static methods defined here:
#  |
#  |  __new__(*args, **kwargs) from builtins.type
#  |      Create and return a new object.  See help(type) for accurate signature.
#  |
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:
#  |
#  |  __isabstractmethod__
#  |
#  |  fdel
#  |
#  |  fget
#  |
#  |  fset
#       property() 装饰器有三种管理属性的
#       就可以 访问方法名的方式 达到属性只读的目的
#       而且如果试图 添加属性则会报错，
# 
#
# -------------------- 自定义读取私有属性的实例方法
#              
class Dog(object):
    """docstring for Dog
        1.0 在初始化实例方法里面设置一个私有属性
        2.0 创建一个获取私有属性的方法
        3.0 实例化通过调用 这个获取私有属性的 方法，从而查看这个私有化属性
        ------ 注意点：
                    这样这个私有化属性只可以查看，不可以修改
                    如果试图在实例化对象里面修改这个私有属性 
                    那么请注意，你并没有修改那个私有属性，
                    而是在实例化对象里面 重新创建了一个新的属性
                    因为 私有化属性系统会自动改名，把原来的私有属性名
                    改成 _类__私有属性名 这样的格式 储存在__dict__ 字典里面
                    那么如果你想在类的外面直接修改和查看 ， 就必须按照这种格式的
                    属性名进行操作，但是，并不提倡这样做，因为违背了属性私有化的初衷

    """
    def __init__(self):
        self.__name = "bruce"
    def getAttr(self):
        """
        直接在外界调用这个方法就可以查看 私有化属性的值
        """
        return self.__name
d = Dog()
print(d.__dict__)


# ----------------- 用property()函数来做私有属性的 查 改 删
# 
class Persen(object):
    """docstring for ClassName"""
    def __init__(self):
        self.__name = "bruce"
    def getname(self): return self.__name
    def setname(self, value): self.__name = value
    def delname(self): del self.__name
    name = property(getname, setname, delname)
p = Persen()
# 查
print(p.name)
# 改
p.name  = "zhu"
# 删
del p.name
print(p.__dict__)

# ------------------- 用@property装饰装饰器 来装饰 操作私有化属性的方法
#                       @property 装饰查询私有化属性的函数
#                       @name.setter 装饰设置私有化属性的函数
#                       @name.deleter 装饰删除私有属性的函数
class Car(object):  
    def __init__(self):
        self.__color = "red"
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self,val):
        self.__color = val
    @color.deleter
    def color(self):
        del self.__color

mpv = Car()
# 曾
print(mpv.color)
# 改
mpv.color = "black"
# # 删
del mpv.color
print(mpv.__dict__)

# ------------------------- __setattr__拦截外界对类属性的操作
# 
class Phone(object):
    """docstring for ClassName
    __setattr__ 只要有 实例.属性 = 值 的语句都会自动调用这个方法
    """      
    def __setattr__(self,key,value):
        if key == "color" and key in self.__dict__.keys():
            print("只读属性不能修改")
        else:
            self.__dict__[key] = value
    def __getattr__(self,key):
        print("getattr")
ipone = Phone()
ipone.color = "red"
ipone.color = "balck"
# --- __getattr__ 当外界用过实例查找属性的时候 ，如果实例没有，那么就会找类里面的
#   如果类里面没有 就会 找父类里面的 如果父类没有 就会调用 __getattr__方法
print(ipone.__dict__)
print(ipone.color)
        
