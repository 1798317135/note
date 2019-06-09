# ##################### 多任务 #########################
# 
# 1.0 多任务可以让多个函数一起执行
# 2.0 多任务的一种实现方式就是多线程
# 3.0 多任务可以用threading 模块
# 4.0 并行是真的多任务
#     因为并行是每个任务一同执行,互不干扰
#     
# 5.0 并发是假的多任务
#     因为 并发是在一个时间切片当中,每个任务轮流执行,
#     因为比较块所以看起来像同时执行一样
# 
# 6.0 python在运行程序的时候,自己自带了一个主线程
#     当我们用threading.Thread(target = 指定的程序)
#     这个时候系统在创建一个子线程,回去执行这个线程指定的任务
#     
# 7.0 当主线程死掉的时候 子线程必死无疑,不会继续执行
#     我们也可以让主线程 等待子线程执行玩后,一起死掉

# 8.0 Threading.enumerate() 这个类可以查看这个程序中所有的线程
#     并返回一个列表
# 
# 9.0 每个线程的运行顺序是不确定的,每次都不一样
# 
# 10.0 如果子线程指定执行的程序运行完毕,也就意味值这个子线程的结束.
# 
# 11.0 线程的创建是在threading创建出的线程对象开始执行start()方法的时候，线程开始创建，并执行
#      线程的结束是在函数执行结束
#      start() 开启子线程的方法 默认情况下 主线程和 子线程一起往下执行,当主线程结束时 子线程仍然运行
#      如果 想让主线程阻塞等待 子线程的结束 我们需要用到join()方法
#      join()调用 这个方法的子线程 会让主线程阻塞等待他的完成 然后主线程才往下走，并不影响其他线程
#      
# 12.0 有时候我们需要将主线程设置为守护线程，也就是当主线程结束后，子线程无论是否结束 都随着
#       主线程的结束而结束
#       这个需要用在子进程之前调用这个方法
#       setDaemon(True) 
# 
# 线程提供的类
# Thread, Lock, Rlock, Condition, [Bounded]Semaphore, Event, Timer, local。
# 
# 常用分方法
# threading.currentThread(): 返回当前的线程变量。 
# threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。 
# threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。      
# 
# threading 模块提供的常量
# threading.TIMEOUT_MAX 设置threading全局超时时间。
#  
import time
import threading

##################### threading.Thread
# def sing():
#     for x in range(5):
#         print("----正在唱歌:菊花台------\n")
#         time.sleep(1)
#         print("song over")

# def danser():
#     for x in range(5):
#         print("-----正在跳舞----------\n")
#         time.sleep(1)
#         print("dance over")

# def main():
#     thread = []
#     t1 = threading.Thread(target = sing)
#     thread.append(t1)
#     t2 = threading.Thread(target = danser)
#     thread.append(t2)
#     for t in thread:
#         # t.setDaemon(True) #当主线程结束 不再等待子线程
#         t.start()
#     t1.join() # 主线程阻塞等待.子线程

# if __name__ == "__main__":
#     start = time.time()
#     main()
#     for i in threading.enumerate():
#         print(i)

#     end = time.time()
#     print(end - start)
#     print("all over")
#     
############################ 封装Thread类
#
# ---- 如果一个线程里面需要实现的复杂的代码，我们可以把这一部分代码
#      封装到一个类里面，并让这个类继承 Threading.thread这个类
#      然后在run方法里面实现
#      外面直接可以调用start()方法来创建和启动这个实例对象的线程来执行run方法里面的代码
#      
#      --- 需要重写__init__()方法

    
# import gevent
# from gevent import monkey
# monkey.patch_all()

# class Mythread(threading.Thread):
#     def __init__(self):
#         super().__init__()

#     def run(self):
#         gevent.joinall([
#         gevent.spawn(self.test2),
#         gevent.spawn(self.test1)
#     ])

#     def test1(self):
#         for x in range(5):
#             print("唱歌")
#             time.sleep(1)
#             print("唱歌结束")

#     def test2(self):
#         for x in range(5):
#             print("跳舞")
#             time.sleep(1.2)
#             print("跳舞结束")


# m = Mythread()
# # m.setDaemon(T)
# m.start()
# m.join()
# print("over")



########################### 多线程共享全局变量
#
# 多线程之间是共享全局变量的
# 我们可以把他们公用的的变量放到全局，来让全部的线程共享
# 共享数据可以让多个线程共同完成任务，来实现多任务的价值

# num = 0
# lock = threading.Lock()
# def test1():
#     global num
#     for x in range(1000000):
#         lock.acquire()
#         num += 1
#         lock.release()
#     print(num)

# def test2():
#     global num
#     for x in range(1000000):
#         lock.acquire()
#         num += 1
#         lock.release()
#     print(num)

# lis = []
# m1 = threading.Thread(target = test1)
# m2 = threading.Thread(target = test2)
# lis.append(m1)
# lis.append(m2)
# for x in lis:
#     x.start()
# x.join()
# print(num)


############################ 给线程传递参数args
#
# 除了共享全局变量,也可以给线程指定的函数 传递参数 args = ()
# args 传递的一定是一个元祖，如果是一个的话后面加上逗号，

# def t1(*args):
#     print(args)

# def t2(*args):
#     print(args)

# def main():
#     aa = threading.Thread(target=t1,args = (1,4))
#     bb = threading.Thread(target=t2,args = (3,[4]))
#     aa.start()
#     time.sleep(1)
#     bb.start()
#     # print(lis)

# if __name__ == "__main__":
#     main()

# ######################### 资源竞争
# 当资源共享的时候,就会出现资源竞争的问题
# 因为操作系统在调度线程时候是不确定的，
# 有可能在一个线程正在操作共享数据的时候，被系统中断，就会出现结果的错误，
# 违背数据的原子性，也就是不可分割
# num = 0

# def t1():
#     global num
#     for i in range(1000000):
#         num += 1

# def t2():
#     global num
#     for i in range(1000000):
#         num += 1

# def main():
#     aa = threading.Thread(target=t1)
#     bb = threading.Thread(target=t2)
#     aa.start()
#     bb.start()
#     time.sleep(10)
#     print(num)


# if __name__ == "__main__":
#     main()

################# 互斥锁
#
# 当两个线程同步执行共享数据的时候
# 为了解决资源竞争问题，我们可以给他上锁
# 也就是说在一个线程执行锁里面的数据的时候另一个线程等待上一个锁的解开
# 然后才会执行自己锁里面的代码，以此类推
# 这样可以保护数据的原子性
# 这个锁默认是解开的
# 我们需要通过threading.lock()这个锁对象 他可以创建一个锁对象
# 然后各个线程只能用这一把锁
# l.acquice()上锁
# l.release()解锁
# 锁的越小越好
# 
# num = 0
# def t1(loker):
#     global num
#     for i in range(1000000):
#         loker.acquire()
#         num += 1
#         loker.release()

# def t2(loker):
#     global num
#     for i in range(1000000):
#         loker.acquire()
#         num += 1
#         loker.release()

# def main():
#     loker = threading.Lock()
#     aa = threading.Thread(target=t1 ,args = (loker,))
#     bb = threading.Thread(target=t2 ,args = (loker,))
#     aa.start()
#     bb.start()
#     time.sleep(5)
#     print(num)


# if __name__ == "__main__":
#     main()

########################### 死锁
#每个线程可以有多个锁
#死锁是一种状态
#当a的一把锁在等待b的解开
#b的一把锁在等待a的解开
#这样就卡在那里
# --- 解决死锁问题
#     第一  我们可以使用 递归锁 Rlock()来创建锁
#     第二 信号量Semaphore() 来创建锁
#     


# class MyThread(threading.Thread):
#     def __init__(self,a,b):
#         super().__init__()
#         self.a = a
#         self.b = b

#     def run(self):
#         self.test1()
#         self.test2()

#     def test1(self):
#         self.a.acquire()
#         print("拿到A锁")
#         self.b.acquire()
#         print("拿到B锁")
#         self.b.release()
#         self.a.release()

#     def test2(self):
#         self.b.acquire()
#         print("拿到B锁")
#         self.a.acquire()
#         print("拿到A锁")
#         self.a.release()
#         self.b.release()

# if __name__ == "__main__":
#     a = b = threading.Lock()
#     a = b = threading.RLock()
#     for i in range(10):
#         m = MyThread(a,b)
#         m.start()
################### 生产者与消费者
# lock 只能解决简单的单一的线程同步造成资源竞争问题
# 如果更复杂的竞争就需要考虑Condition(条件变量这种方式)
# 他的主要逻辑是：
#   程首先acquire一个条件变量 然后去判断条件变量是否符合
#   如果不符合就wait 如果符合就做一个写改变 然后用 notify 通知其他处于wait的进程
#   重复这个过程可以解决复杂的同步问题
# 可以用生产者与消费者模型来演示
# 首先生产者和消费者各占一个线程 ，然后双方围绕products产品来产生同步问题
# 让2个生产者生产品 让10个消费者消耗产品
# 
import threading
import time
 
condition = threading.Condition()
products = 0
 
class Producer(threading.Thread):
    '''生产者'''
    ix = [0] # 生产者实例个数
             # 闭包，必须是数组，不能直接 ix = 0
    def __init__(self, ix=0):
        super().__init__()
        self.ix[0] += 1
        self.setName('生产者' + str(self.ix[0]))
 
    def run(self):
        global condition, products
        
        while True:
            if condition.acquire():
                if products <= 50:
                    products += 10;
                    print("{}：库存不足(10-)。我努力生产了1件产品，现在产品总数量 {}".format(self.getName(), products))
                    condition.notify()
                else:
                    print("{}：库存充足(10+)。让我休息会儿，现在产品总数量 {}".format(self.getName(), products))
                    condition.wait();

                condition.release()
                time.sleep(2)


class Consumer(threading.Thread):
    '''消费者'''
    ix = [0] # 消费者实例个数
             # 闭包，必须是数组，不能直接 ix = 0
    def __init__(self):
        super().__init__()
        self.ix[0] += 1
        self.setName('消费者' + str(self.ix[0]))
 
    def run(self):
        global condition, products
        
        while True:
            if condition.acquire():
                if products > 1:
                    products -= 1
                    print("{}：我消费了1件产品，现在产品数量 {}".format(self.getName(), products))
                    condition.notify()
                else:
                    print("{}：我停止消费。现在产品数量 {}".format(self.getName(), products))
                    condition.wait()
                condition.release()
                time.sleep(2)



if __name__ == "__main__":
    for i in range(2):
        p = Producer()
        p.start()
 
    for i in range(10):
        c = Consumer()
        c.start()

#################### 线程池

# 服务器端最佳线程数量=((线程等待时间+线程cpu时间)/线程cpu时间) * cpu数量
# 我们提前预先准备好对于电脑性能最合适的线程数，然后让这个线程池自动调度,提高性能

# from concurrent.futures import ThreadPoolExecutor,ALL_COMPLETED,FIRST_COMPLETED,FIRST_EXCEPTION
# import sys,os,shutil,concurrent.futures,random,threading,queue
# clock = threading.Lock()
# def file_copy(old_folder_name,new_folder_name,file,q):
#     name = shutil.copy(os.path.join(old_folder_name,file),os.path.join(new_folder_name,file))
#     q.put(file)
#     return name 

# def main():
#     #1.0  获取原始文件夹，判断是否是文件
#     old_folder_name = input("请输入复制的文件夹:")
#     if not os.path.isdir(old_folder_name):
#         print("问价夹不存在")
#         main()

#     # 2.0 创建新的问价夹new_floder_name并判断是否存在
#     new_folder_name = old_folder_name+"[复件]"
#     if not os.path.exists(new_folder_name):
#         os.mkdir(new_folder_name)

#     # 3.0 获取源文件里面的所有文件
#     file_list = os.listdir(old_folder_name)

#     # 4.0 创建线程池
#     pool = ThreadPoolExecutor(max_workers = 5)
    
#     # 5.0 创建一个队列对象
#     q = queue.Queue()

#     # 6.0 网线程池里面之执行函数
#     futures = [pool.submit(file_copy,old_folder_name,new_folder_name,file,q) for file in file_list]
#     pool.shutdown(wait=True)
#     # 7.0 判断完成的数是否等于总数
#     lens = len(file_list)
#     idx = 0
#     while True:
#         q.get()
#         idx += 1 
#         print("已完成{0:.2f}%".format(idx / lens * 100))
#         if idx >= lens:
#             break

#     # 释放内存
    

# if __name__ == "__main__":
#     main()

