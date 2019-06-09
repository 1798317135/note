#  
#  1.0 静态方法 是用staticmethod后面，被修饰的方法
#  2.0 静态方法没有限制参数，可以没有任何参数
#  3.0 因为这个静态方法是在类里面 所以这个静态方法只能访问类属性 不能访问实例属性
class Persen:
    @staticmethod
    def run():
        print("这个是静态方法")
class aa(Persen):
    pass
yang = aa()
bruce = Persen()
# 静态方法可以被 类 ，实例，子类调用
Persen.run()

bruce.run()

aa.run()

yang.run()

bb = Persen.run
bb()