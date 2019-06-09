#  type元类是所有类的祖宗，在python中任何类都是 有元类实例化出来的对象
#  元类是最上面的类
#  每个对象都可以使用__class__来查询实例化他的类
class Persen:
    pass

num =  12
str = "aaa"
tuple = (1,2,3,4)
dict = {"name":"yang","age":18}
list = [1,2,3,45]
set = {1,2,3,4,5}
mj = enumerate("adfasdf")
it = iter("asdfasdf")

# 都是返回的type 类型的元类 他实例化出所有类
print(num.__class__.__class__,"num类型")
print(str.__class__.__class__,"str类型")
print(tuple.__class__.__class__,"tuple类型")
print(dict.__class__.__class__,"dict类型")
print(list.__class__.__class__,"dict类型")
print(set.__class__.__class__,"set类型")
print(mj.__class__.__class__,"枚举对象")
print(it.__class__.__class__,"迭代器")
print(Persen.__class__.__class__,"Persen")

# ***************************  注意點 **********************************
# 
# --- 並不是多有的類，都是由type元类創建的。
# 
#     每当创建一个类的时候 ，系统会自动检索是否存在 指明创建这个类的元类
#     
#     如果存在指向的元类，那么就会用这个指向的元类去创建这个类，而不会用type元类去创建。
#     
#     他的检索元类的顺序是
#     先从 类检索是否指明元类 如果没有
#     然后 在他父类里面找 如果没有
#     然后会在整个模块里面找 如果没有
#     然后才会用type 创建
#       
# --- __metaclass__可以指明创建这个类的元类
#     --- 他的作用是
#         1.0 可以拦截类的创建
#         2.0 可以修改类
#         3.0 可以返修改之后的类
#         4.0 
#      
# 
# 1.0在模块里面指明
__metaclass__ = xxx

# 2.0 在父类里面指向
class Father:
    __metaclass__ = xxx

# 3.0 在子类里面指向
class Son(Father):
    __metaclass__ = xxx

# 4.0 
class Persen(metaclass = xxx):
    pass