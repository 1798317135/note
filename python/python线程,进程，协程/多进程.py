# 多进程也是完成多任务的方式
# 多进程用法和多线程差不多
# 进程之间的数据传递，可以通过
# socket，队列，文件，或者用数据库缓存来实现进程之间的通信
# 队列可以用到multiprocessing.queue这个类

# import multiprocessing
# import time
#     print("数据入队列")
#     for i in range(1,10):
#         pass

# def test2(data):
#     print(2)

# def main():
#     q = multiprocessing.queues()
#     p1 = multiprocessing.Process(target = test1,args = (q,))
#     p2 = multiprocessing.Process(target = test2, args = (q,))
#     p1.start()
#     p2.start()
# if __name__ == '__main__':
#     main()
# 
#  ##################### 进程之间的通信

# from multiprocessing import Queue
    # q = Queue(3) #表示这个队列里面最多放三个数据
    # q.put(1) #往这个队列里面放入数据
    # q.get() #从队列里面取数据
    # q.size() #获取队列大小
    # q.full() #判断是否满了
    # q.empty() #判断是否空了
    # def test1(data):

# def put_(q):
#     lis = [1,2,3,4,5,6,7,8,9,7]
#     for i in lis:
#         if q.full() != True:
#             q.put(i)
#         else:
#             continue
#     print("-"*5)

# def get_(q):
#     while True:
#         if q.empty() != True:
#             print(q.get())
#         else:
#             break
# def main():
#     q = Queue(6)
#     m1 = multiprocessing.Process(target = put_, args = (q,))
#     m2 = multiprocessing.Process(target = get_, args = (q,))
#     m1.start()
#     m2.start()

# if __name__ == "__main__":
#     main()
# 
# 
# ######################### 进程池
# 
# 进程池也就是预先开好进程数,需要的时候自动调度。可以节省资源
# 进程池的进程数，按照电脑配置，来达到最高效率
# os.getpid()可以获取进程号
# p.close() 可以关闭进程池子
# p.join() 等待子进程完成
# 
# 进程池之间的通信时通过
# from multiprocessing.managers import queue
# print(queue.Queue())
# 
# 
# from multiprocessing import Pool
# import time,random,os

# def worker(msg):
#     t_start = time.clock()
#     print("{}开始执行,进程号为{}----------".format(msg,os.getpid()))
#     # time.sleep(random.random())
#     t_end = time.clock()
#     print("{}执行完毕,用时{}".format(msg,t_end - t_start))

# def main():
#     p = Pool(3)
#     for i in range(10):
#         p.apply_async(worker,(i,))
#     p.close()
#     p.join()

# if __name__ == "__main__":
#     main()

    