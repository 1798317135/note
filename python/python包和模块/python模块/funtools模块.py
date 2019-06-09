import functools

# --- 1.0 functools.partial 设置偏函数

def persen(*args,**Keywords):
    print(*args,Keywords)
    # print(Keywords["name"][0])
persen(1, 2, 3, 4)
persen = functools.partial(persen,name = "yang")
persen(2,3,4)

# --- 2.0 @functools.total_ordering 叠加比较方法 装饰器
# 
@functools.total_ordering
class Persen:
    def __init__(self,age):
        self.ages = age
    def __eq__(self,other):
        print("等于")
        return self.ages == other.ages
    def __gt__(self,other):
        print("大于")
        return self.ages > other.ages
p = Persen(18)
p1 = Persen(19)
print(p >= p1)