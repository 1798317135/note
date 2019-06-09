class Animal:
    age = [18] 
    def run(self):
        print("跑",self)

class Dog(Animal):
    pass

class Cat(Animal):
    pass

d = Dog()
d.age = 418
print(d.age)
print(d.__dict__)
print(Animal.__dict__)

