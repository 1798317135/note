################################### 生成器 ######################################
#
# 1.0 生成器是一个特殊的迭代器(迭代器的抽象层级更高)
# 
# 2.0 生成器拥有迭代器的特性 
#       1. 惰性计算数据 节省内存，
#       2 next()递增指针 每次调用都会会记录位置，并自增
#       3 可迭代性
# 
#
# ################################## 生成器的创建 ################################
# 
# *********** 生成器表达式进行创建 ***********
# --- 把列表生成式的[] 改为 ()就是生成器推导式
# 
# generator = (num for num in range(0,11) if num %2 ==0)
# print(generator,"generator")
# print(next(generator))
# print(next(generator))
# print(generator.__next__())
# 
#  
# ***********生成器函数进行创建 ************** 
# 
# --- 用函数进行创建，
#     但是函数必须包含yield语句
#     这个函数的执行结果就是一个生成器
#     
# --- yield 可以阻断函数，暂停到yield这里 
#     通过next()或者__next__()把生成器的指针往后移动到下一个yield
#     如果执行到最后一个yield的时候 再次移动指针会报错 StopIteration
# def generator():
#     print("111")
#     yield 1
#     print("aa")
#     yield 2
#     print("bb")
#     yield 3
#     print("cc")
# result = generator()
# print(result)
# print(next(result))
# print(next(result))
# print(next(result))

# --- 生成器每次调用自增1
def add():
    aa = 0
    while True:
        aa += 1
        yield aa
result = add()
print(next(result))
print(next(result))
print(next(result))
print(next(result))

# --- send()可以给上一句 yield语句传值 如果要第一次调用 注意把穿的值是一个空值none 不然会报错

def test():
    print("xxx")
    result1 = yield 1
    print(result1,"1")
    result2 = yield 2
    print(result2,"2")
result = test()
print(result.send(None))
print(result.send("11"))

# print(result.__next__())
# 
# --- .close()关闭生成器 后面在用调用指针则会报错
def test1():
    yield 1
    yield 2 
    yield 3
result = test1()
print(result.__next__())
result.close()

# --- return 碰到return 语句会直接终止 并抛出 StopIteration 返回值
def test2():
    yield 1
    yield 2
    yield 3
    return 10
result = test2()
print(result)

# 生成器 和迭代器一样不能重复使用
def test3():
    yield 1
    yield 2
    yield 3
result = test3()
for x in result:
    print(x)
print("-------")
for x in result:
    print(x)