import functools

@functools.total_ordering
class Persen:

####################################### 格式化操作方法 #########################################

    def __init__(self,n,a):
        """
        实例属性初始化方法
        每个实例都会自动调用这个方法
        """
        self.name = n
        self.age = a
        self.cache = {}
        self.item = []
        self.index = 0
    def __str__(self):
        """
        信息格式化方法 
        每当 在外界打印 实例的时候 就会自动调用这个方法
        str(实例) 函数也会调用这个方法
        返回值就是实例打印的结果
        他是面向用户的返回结果是可视的
        """
        return "这个人的姓名是{0},这个人的年龄是{1}".format(self.name,self.age)

    def __repr__(self):
        """
        如果类里面没有实现__str__ 这个方法
        那么打印实例 或者 用repr()可以触发这个方法
        在交互模式下 直接输入实例就会打印 这个方法返回的结果
        返回值 就是打印的结果
        他面向的是开发人员 可以详细打印出对象的 地址 信息等
        可以用eval()函数 将打印结果重新转换成 可读的面向用户的 结果
        """
        return "1+1"
# ################################## 调用操作的方法 ######################################
    def __call__(self,*args,**keyargs):
        """
        如果你直接调用实例 实例() 那么就会触发这个方法
        这个方法的作用，可以让一个实例对象当函数使用的 方法
        __call__ 可以给实例添加参数
        当我们直接把实例当作函数使用的时候就会调用这个方法

        比如说，一个钢笔实例 我们可以用这个方法给实例添加各种颜色等属性
        这个方法的使用场景
        1.0 给实例化传递不同的参数 从而供这个实例使用
        """
        print("我的名字是{name},我的名字是{age}我的身高是{height}".format(*args,**keyargs))

##################################### 索引操作的方法 #######################################
#
#--- 1.0 可以将我们创建的实例对象 以列表或者字典的形式进行操作
#         有 增改 删 查 三个方法
#         我们可以把值存储在初始化方法里面定义的字典或者列表里面
#         
#          
#--- 2.0 这三个方法也可以通过 slice()方法进行切片操作
#        注意切片方法 只可以执行 改 查看 和  删除操作
#        如果我们对 实例索引进行切片操作 
#        那么__setitem__接收的key 就是一个slice类型的属性
#        slice类型的属性有三个参数 start step stop start是切片的开始，step步长，stop 结束
#        我们可以直接在列表里面使用这个类型的数据，进行切片操作
#        也可以把他分解开来 如果是分解来开 进行切片操作 需要进行对key 的类型进行判定
#        如果是slice 类型 那么就可以进行切片操作
#        不然的化 如果key 是一个字符串那么可能就会报错
#       
    def __setitem__(self,key,val):
        """设置方法或者修改方法"""
        if isinstance(key,slice):
            start = key.start
            step = key.step
            stop = key.stop
            self.item[start:stop:step] = val
        else:
            self.cache[key] = val
            
    def __getitem__(self,key):
        """
        获取方法
        也是迭代实例化的方法
        """
        # if isinstance(key,slice):
        #     return self.item[key]
        # else:
        #     return self.cache[key]
        self.index += 1
        if self.index >6:
            raise StopIteration("停止")
        else:
            return self.index
        
    def __delitem__(self,key):
        """删除方法"""
        if isinstance(key,slice):
            del self.item[key]
        else:
            del self.cache[key]

# #################################### 比较操作方法 ####################################
# 
# 1.0 让我们比较两个实例的时候 我们可以通过 一些系统自带的方法 来指定相应的比较规则
# 2.0 python常用的比交符号 有 == ！= < <= > >= 
#     这里的比较方法也是这几种
# 3.0 当我们使用 什么比较符号 就会进入到对应的方法当中
# 
# 4.0 为了节省代码量 我们其实可以用 一个符号 去推导出相反的那个符号 甚至可以叠加 
#      比如用 用 < 推导出 > 用 > 和 =  叠加出 >=  
#      比如 我们在用 我们可以用__eq__判断 ！= 因为只要 系统检测到反向的比较
#      系统会给两个比较的对象 调换位置 或 取反
#      当我们使用 functools里面的 @functools.total_ordering 装饰器 后 可以叠加
#      用 > 叠加 = 会先调用 > 方法 如果返回的false 就会调用 =  
    def __eq__(self,other):
        "等于"
        return self.age == other.age
    # def __ne__(self,other):
    #     "不等于"
    #     return self.age != other.age
    def __gt__(self,other):
        "大于"
        return self.age > other.age
    # def __ge__(self,other):
    #     "大于等于"
    #     return self.age >= other.age
    # def __lt__(self,other):
    #     "小于"
    #     return self.age <= other.age
    # def __le__(self,other):
    #     "小于等于"
    #     return self.age <= other.age
# #################################### 实例化的返回值 bool类型 ####################################
#
# --- 1.0 实例在上下文中的bool值 True 或则 False
# 
# --- 2.0 我们可以利用实例的返回值进行判断
# 
# --- 3.0 这里面控制实例化的bool值
    def __bool__(self):
        return True

# ################################### 实例化 的 遍历操作 ###########################################
# 
# --- 1.0 如果要对一个实例化用 for in 语句 或者 next() 进行遍历的操作 有两种方式
#     --- 第一种 就是 上面我们使用到的__getitem__()这个方法
#          这个方法 可以把对象 当作 字典和 列表 进行读取操作 或者 切片读取的操作
#          也可以把 实例化 用 for in 语句进行遍历
#           这个方法 不能使用 next() 进行取值
#      --- iter（）
#           可以用 iter()方法 将调用这个方法的 实例 转换成 一个迭代器
#           也可以 用 iter(c,t) 这种方式直接把这个方法传递个 第一个参数 知道返回的值 等于后面的值 之前停止
#           
#       --- 注意  必选设置终止 条件 不然就会死循环
#       --- 他遍历实现是机制 就是每次for in 获取这个方法没次调用的返回值

# --- 2.0 实现 __iter__方法 
#          这个方法的优先级 高于__getitem__ 也就是说，我们遍历实例对象的时候 会优先调用这个方法
#          
#         --- 这个方法如果返回的是一个迭代器 那么外界通过操作这个迭代器的自带__next__方法来访问下一个元素
#              如果返回的不是一个迭代器 那么我们需要 给他创建一个 __next__方法 来进行 访问下一个对象
#              
# --- 3.0 __next__ 方法可以用next()对象 访问这个方法的返回值 每次调用 指针往前移一个
#         __next__可以像 __getitem__这样 直接使用 iter()转换成 迭代器 也可以使用 iter()截至到某个返回值停止
# 
# --- 4.0 只要实现了 __iter__ 和 __next__这两个方法那么实例就是一个迭代器
#          如果 只实现了 __iter__那么 这个实例只是一个可迭代对象 
#          注意 --- 可以迭代的不一定是 可以迭代对象
#          但是可迭代对象一定是可以迭代的对象
#         
#         
    def __iter__(self):
        self.index = 0
        return iter([1,2,3,45])
    # def __next__(self):
    #     self.index += 1
    #     if self.index > 6:
    #         raise StopIteration("asdf")
    #     else:
    #         return self.index
p = Persen("bruce", 18)
# # __str__
# print(p)
# # __repr__
# print(repr(p))
# # __calss__
# p(age = 18,name = "yang",height = 180)
# # __setitem__()
p["name"] = "yang"
p["age"] = 18
# print(p.cache)
# # __setitem__切片
p.item = [1,2,3,4,5,6,74,8]
# p[0:3] = ["a","b","c"]
# print(p.item)
# # __getitem__
# print(p["name"])
# # __getitme__切片
# print(p[0:3])
# # delitem__
# del p["name"]
# print(p.cache)
# # __delitem__切片
# del p[0:3]
# print(p.item)
# # __eq__
# p1 = Persen("张",20)
# p2 = Persen("朱",18)
# # print(p1 == p2)
# # # __ne__
# # print(p1 != p2)
# # # __gt__
# # print(p1 > p2)
# # #__ge__
# # print(p1 >= p2)
# # # __lt__
# # print(p1 < p2)
# # # __le__
# # print(p1<=p2)
# # 比较推导
# print(p1 == p2)
# print("-"*5)
# # __bool__ 
# if p1:
#     print(111)

# __getitem__遍历实例
for x in p:
    print(x)
# __iter__
for j in p:
    print(j)
# __next__
# next(p)
# 
import collections
print(isinstance(p,collections.Iterable))
print(isinstance(p,collections.Iterator))
print(callable(Persen))

# __new__可以拦截对象的创建，并返回这个对象，他在__init__方法之前操作
# 可也已在元类里面使用这个方法来拦截类的创建 返回这个类
# 第一步 分配对象内存
# 第二部 返回对象内存引用地址
