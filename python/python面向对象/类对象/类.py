
# ##########################################   类分为两种 #######################
# 
# 1.0 类名首字母需要大写
# 2.0 命名驼峰式命名规则
# 3.0 类有点类似与javascript里面的构造函数
# 
# *****************************************  一种是新式类
# 
# --- 1.0 经典类是pyton3.x 当中定义的类 他默认继承 object类
# 
# --- 2.0 如果想在python2中 运行需要手动的让类继承object类
# 
# --- 3.0 用__bases__ 查看这个类 继承的基类 也就是他的所继承的父类
#         和__class__ 的区别是 __class__ 返回的是构造这个对象的构造器 而不是父类
# 
# ----------- 定义类 
class ClassOld(object):
    pass

className = ClassOld

# --- __name__ 返回变量引用的类名
print(className.__name__)

# -------------- 实例化对象
obj = ClassOld()

# --- __class__ 返回产生此对象的类
print(obj.__class__)



# *********************************************  第二种是经典类
# --- 经典类是没有继承object 的类
#     而新式类是继承了object的类
#     在python3 中类自动继承object 所以python3是新式类
#     而python2 中不会自动继承object 那么这个就是经典类
#     我们可以给python2 当中的经典类手动继承object 即可改为为新式类

# 
#  ------------ 用type() 元类手动创建出一个类
# ---- type(object_or_name, bases, dict) 然后赋值给一个引用创建的这个类的的 任何变量
#      object_or_name 规定创建的类名称
#      bases 继承的内容
#      dict 储存在这个类里面的属性 和方法
def run(self):
    return self

Persen = type ("Persen",(),{"age":18,"name":"杨","run":run})
p = Persen()
p.run()

print(p.run() == p)
print(p.age)
print(Persen.__dict__)
