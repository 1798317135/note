class calculator(object):
    """docstring for ClassName"""
    def __check(func):
        def inner(self,arg):
            if not isinstance(arg,int):
                raise TypeError("当前数据类型不是int")
            return func(self,arg)
        return inner
    @__check
    def __init__(self,arg):
        self.__init = arg
    @__check
    def jia(self,arg):
        self.__init += arg
        return self
    @__check
    def jian(self,arg):
        self.__init -= arg
        return self
    @__check
    def cheng(self,arg):
        self.__init *= arg
        return self
    @__check
    def chu(self,arg):
        self.__init/= arg
        return self
    def show(self):
        print("计算的结果是{0}".format(self.__init))

    @property
    def result(self):
        return self.__init
c = calculator(3)
c.jia(6).cheng(10).chu(3).show()
print(c.result)


        
        