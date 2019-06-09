# 用生成器来实现多任务
# def test1():
#     while True:
#         print(1)
#         yield

# def test2():
#     while True:
#         print(2)
#         yield

# if __name__ == '__main__':
#     for i in range(20):
#         t1 = next(test1())
#         t2 = next(test2())
#  
# 用greenlet 模块来实现协程
# 这个模块进一步对yeild 语句进行了封装 他更对比yeild 更加简单
# 创建一个协程对象 
# 用switch()方法来来进行分配协程


# from greenlet import greenlet
# import time

# def test1():
#     while True:
#         print(1)
#         g2.switch()
#         time.sleep(0.5)

# def test2():
#     while True:
#         g1.switch()
#         print(2)
#         time.sleep(0.5)
    
# g1 = greenlet(test1)
# g2 = greenlet(test2)
# g1.switch()

# 用gevent 来实现协程
# 一般都用gevent 模块来创建协程多任务

# 1.0 他可以根据延迟或者耗时任务来自动调度协程
#     他可以利用延迟的时间去执行其他的事情
#     这也就是协程的特点
# 
# 2.0 他不会识别time.sleep()这个延时
#     他可以识别自己自带的gevent.sleep()这个方法创建的延时操作
#     如果你想让他识别所有延时操作就需要打补丁
#     用monkey这个模块
#     monkey.patch_all() 这样就无需更改代码来识别所有的延时操作
#     
# 3.0 # 用spawn()方法来生成协程对象
# 
# 4.0 用.join()来开始调度每个协程对象
#     但是每个协程对象都需要手动的来.join()来开启
#     我们可以用gevent.joinall()来把所有的协程对象放进去
#     他根据所有的协程对象的延时操作来自动调度里面的协程对象
#     他接收一个列表，我们可以把协程对象封装成一个列表放进去

import gevent,time
from gevent import monkey
monkey.patch_all()
def t1(n):
    for i in range(n):
        print("t1")
        time.sleep(3)

def t2(n):
    for i in range(n):
        print("t2")
        time.sleep(1)

def t3(n):
    for i in range(n):
        print("t3")
        time.sleep(2)

# print("-----1-------")
# g1 = gevent.spawn(t1,5)
# print("-----2-------")
# g2 = gevent.spawn(t2,5)
# print("-----3-------")
# g3 = gevent.spawn(t3,5)
# print("-----4-------")
# g1.join()
# g2.join()
# g3.join()

gevent.joinall([
    gevent.spawn(t1,5),
    gevent.spawn(t2,5),
    gevent.spawn(t3,5),
    ])






