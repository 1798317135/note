# ---  多态是不同的子类调用同一个父类，产生不同的执行结果
# 1.0 多态可以增加代码的灵活度
# 2.0 以继承 和 重写父类方法的前提下
# 3.0 是调用方法的技巧，不会影响到类内部的设计
class Dog:

    def __init__(self,name):
        self.name = name

    def game(self):
        print("{}狗在玩耍".format(self.name))

class XiaoTianDog(Dog):

    def game(self):
        print("{}飞到天上玩耍".format(self.name))

class Person:

    def __init__(self,name):
        self.name = name

    def with_dog(self,dog):
            print("{}和{}在一起玩耍".format(self.name,dog.name))
            dog.game()

d = Dog("小黑")
x = XiaoTianDog("哮天犬")
p = Person("小明")
p.with_dog(x)