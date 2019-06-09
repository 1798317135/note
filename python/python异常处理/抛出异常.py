# 我们可以手动的抛出异常
# --- raise 语句
#

class jisuan:
    def __init__(self,arg):
        try:
            if not isinstance(arg,int):
                raise ValueError("值错误")
            else:
                print(arg)
        except Exception as e:
            print(e)
            print("错误类型{}".format(e.__class__))

jisuan("sd")