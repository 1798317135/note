# 所有的异常类 都是继承 BaseException 这个类
# 所以自己定义的 异常类 也需要继承这个类

class LessZero(Exception):

    def __init__(self,msg,code_error):
        self.msg = msg
        self.code = code_error

    def __str__(self):
        return "{0},错误码{1}".format(self.msg,self.code)

name = -5
try:
    if name < 0:
        raise LessZero("小于零","404")
        
except LessZero as e:
    print(e)