# ###############################  抽象类 ############################################
# 
#  1.0 抽象类是指 ，不能直接调用 和 实例化的类
#      抽象类用于保存，子类的公有的属性，和方法
#      比如说 猫 和 狗 会叫所以我们把 叫这个方法
#      储存到 动物这个抽象类 ，每个继承 这个类的 类都会
#      继承这些公有属性，方法
#      
#  2.0 python 并不能直接的实现 抽象的类
#      需要借助 abc 这个模块创建抽象类
#      --- abc 模块创建抽象类
#      --- 第一步指定 抽象类的元类，为abc.ABCmeta 用__classmate__内置方法实现
#          或者 直接在继承里面修改
#      --- 第二步 装饰器械 装饰抽象类里面 的方法
#      --- 继承 这个抽象类的类 必须实现 抽象类里面的全部方法
#      
import abc
class Animal(object,metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def run(self,who):
        print("{0}跑".format(who))
    # @abc.abstractclassmethod
    # def eat(self):
    #     print("吃")
class Dog(Animal):
    def run(self,who):
        super().run("狗仔")
    # @classmethod
    # def eat(self):
    #     print("狗在吃")
class Cat(Animal):
    def run(self,who):
        super().run(who)
# a.run()
d = Dog()
d.run("狗")
c = Cat()
c.run("猫")

a = Animal()