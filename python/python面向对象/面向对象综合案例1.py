# 1.0 定义三个类,小狗,小猫,人
# 2.0 小狗:姓名,年龄(默认是一岁) ：吃饭，玩，睡觉，看家 (格式:名字是xx，年龄是xx岁的小狗 在 xx)
# 3.0 小猫:姓名,年龄(默认是一岁) ：吃饭，玩，睡觉，捉老鼠 (格式:名字是xx，年龄是xx岁的小猫 在 xx)
# 4.0 人:姓名,年龄(默认是一岁) ：宠物，吃饭，玩，睡觉(格式:名字是xx，年龄是xx岁的人 在 xx)
# 5.0 养宠物（让所有的宠物吃饭，玩，睡觉）
# 6.0 让宠物工作(让宠物根据自己的职责开始工作)
import abc
class Animal(metaclass = abc.ABCMeta):
    
    @abc.abstractmethod
    def __init__(self,*args,**keywords):
        self.keywords = keywords
        self.name = keywords["name"]
        self.age = 1 if "age" not in keywords else keywords["age"]

    def eat(self):
        print("{0}在吃饭".format(self))
        return self

    def play(self):
        print("{0}在玩".format(self))
        return self

    def sleep(self):
        print("{0}在睡觉".format(self))
        return self

class Dog(Animal):
    def __init__(self,*args,**keywords):
        super().__init__(*args,**keywords)

    def __str__(self):
        return "名字是{},年龄是{}岁的小狗".format(self.name,self.age)

    def work(self):
        print("{0}在看家".format(self)) 
        return self   

class Cat(Animal):
    def __init__(self,*args,**keywords):
        super().__init__(*args,**keywords)

    def __str__(self):
        return "名字是{},年龄是{}岁的小猫".format(self.name,self.age)

    def work(self):
        print("{0}在捉老鼠".format(self)) 
        return self

class Persen(Animal):
    def __init__(self,*args,**keywords):
        super().__init__(*args,**keywords)
        self.pets = keywords["pets"]

    def __str__(self):
        return "名字是{},年龄是{}岁".format(self.name,self.age)

    def yang_pets(self):
        for pet in self.pets:
            pet.eat().play().sleep()
        return self

    def make_pets_work(self):
        for pet in self.pets:
            pet.work()
        return self

d = Dog(name = "小黑",age = 18)
d.eat()

c = Cat(name = "小花")
c.eat()

p = Persen(name = "bruce",pets = [d,c])
p.make_pets_work()
