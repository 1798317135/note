# 我们把类的注释写在类的开头
# 用""""""三个双引号包裹
# 把类属性的注释也写在这个里面
# 如果写在外面 help()将无法查看

# 方法的注释写在方法的开头 用三个引号对包裹
class Persen:
    """
    这个是一个人类
    Attributes:
    sex: 性别
    name： 姓名
    height: 身高
    """
    sex = "男"
    name = "bruce"
    height = 180
    def run(self,where):
        """
        这是一个跑的实例方法
        """
        print("{0}在{1}跑步".format(name,where))


# 用help()方法 快速生成类的注释

help(Persen)