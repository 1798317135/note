# ######################### 线程池和进程池
# 
# 1.0 python 内置的threading 和 multiprocessing 模块可以完成多进程和多线程的创建
# 2.0 但是频繁的创建和销毁线程或进程是很消耗资源的，这个时候我们就可以用到进程池和线程池
# 3.0 从python3.2 之后 标准库种提供了concurrent.futures 模块，
#      他提供支持ThreadPoolExecutor线程池 和 ProcessPoolExcutor 进程池 操作
#      实现了对threading 和multiprocessing 的进一步抽象
# 
# concurrent.futures.Executor 这是一个实现线程池和进程池的抽象类,所以我们只能操作他的子类
#       1.0 submit(fn,*args,**kwargs) 将可调用的fn调度为执行， 并返回表示可调用执行的对象
#       
import concurrent.futures,time

# with concurrent.futures.ThreadPoolExecutor(max_workers = 3) as executor:
#     start = time.time()
#     future = executor.submit(pow,100,10)
#     print(future.result())
#     end = time.time()
#     print("执行时间为{}".format(end - start))

#       2.0 map(func,*iterables,timeout = None,chunksize = 1)
#           iterables 把立即收集到的数据传递一个funcs
#           func以异步方式执行，并且可以多次调用func函数
#           返回一个迭代器
#           timeout 只执行单次任务的时间 如果超出报错
#           chunksize 把可迭代对象分为几块 每块的大小对于很长的可迭代对象 增加这个数可以提高性能


# with concurrent.futures.ThreadPoolExecutor(max_workers = 3) as executor1:
#     start = time.time()
#     future = executor1.map(pow,(100,),(100,),timeout = 1,chunksize = 3)
#     for i in future:
#         print(i)
#     end = time.time() 
#     print("执行时间为{}".format(end - start))

#      3.0  shutdown(wait = True)
#       当使用with 语句的时候避免了shutdown 默认为 True
#       
# import shutil
# with concurrent.futures.ThreadPoolExecutor(max_workers=4) as e:
#     e.submit(shutil.copy, '../python文件操作/案例/dis/avi/3ZuG-qG93.avi', 'dest1.txt')
#     e.submit(shutil.copy, '../python包和模块/包和模块的概念.py', 'dest2.txt')
#     e.submit(shutil.copy, 'src3.txt', 'dest3.txt')
#     e.submit(shutil.copy, 'src4.txt', 'dest4.txt')

############# 线程池的死锁
           
# import time
# from concurrent.futures.thread import ThreadPoolExecutor


# def wait_b():
#     time.sleep(3)
#     print(b.result(),"b")
#     print(123)

# def wait_a():
#     time.sleep(3)
#     print(a.result(),"a")

# executor = ThreadPoolExecutor(max_workers = 1)
# a = executor.submit(wait_b)
# b = executor.submit(wait_a)
# print(a.result())
# print(b.result())
# def wait_on_future():
#     f = executor.submit(pow, 5, 2)

#     # This will never complete because there is only one worker thread and
#     # it is executing this function.
#     print(f.result())

# executor = ThreadPoolExecutor(max_workers=2)
# executor.submit(wait_on_future)
# 
# ################### 线程池详解
# from concurrent.futures import ThreadPoolExecutor
# executor = ThreadPoolExecutor(max_workers=None,thread_name_prefix="",initializer=None,initargs=())
    # max_workers 最大线程池子类，以异步调用
    # initializer 是一个可选的callble，在工作线程的开头调用
    # initargs 传递给初始化的参数元祖，如果初始化异常

# wait(fn,timeout = None, return_when=ALL_COMPLETED)方法可以让主线程阻塞等待子线程的完成
    # 方法接收3个参数，等待的任务序列、超时时间以及等待条件
    # return_when 默认等于ALL_COMPLETED 也就是等待所有子线程的完成
    

# import concurrent.futures
# from concurrent.futures import ThreadPoolExecutor
# import urllib.request,time

# URLS = ['http://www.baidu.com/',
#         'http://www.taobao.com/',
#         'http://www.soso.com/',
#         'http://www.zhihu.com/',
#         'http://www.youdao.com/',
#         ]

# def load_url(url,timeout):
#     with urllib.request.urlopen(url,timeout = timeout) as conn:
#         return conn.read()

# with ThreadPoolExecutor(max_workers=5) as executor:
#     # results = executor.map(load_url,URLS)
#     future_url = {executor.submit(load_url,url,1):url for url in URLS}
#     for future in concurrent.futures.as_completed(future_url):
#         url = future_url[future]
#         try:
#             data = future.result()
#         except Exception as e:
#             raise e
#         else:
#             print(url,len(data))

############### 进程池ProcessPoolExecutor
#
# import concurrent.futures
# import math
# # 1.0 这个进程池 在交互模式下不起作用

# # class concurrent.futures.ProcessPoolExecutor（max_workers = None，mp_context = None，initializer = None，initargs =（））
# # --- max_workes 最大的进程数量
# # --- mp_context 可以控制工作的
# PRIMES = [
#     112272535095293,
#     112582705942171,
#     112272535095293,
#     115280095190773,
#     115797848077099,
#     115797848077097
#     ]

# def is_prime(n):
#     if n % 2 == 0:
#         return False

#     sqrt_n = int(math.floor(math.sqrt(n)))
#     for i in range(3, sqrt_n + 1, 2):
#         if n % i == 0:
#             return False
#     return True

# def main():
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         # print(executor.map(is_prime,PRIMES))
#         for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
#             print('%d is prime: %s' % (number, prime))

# # 该__main__模块必须可由工作程序子进程导入。这意味着ProcessPoolExecutor在交互式解释器中不起作用
# # 
# if __name__ == '__main__':
#     main()

###########################   Future对象
# --- 1.0 Future是由Executor.submit()创建
#     cancel（） # 取消调用,如果无法取消返回False 否则返回True
    # cancelled() #如果成功取消返回Ture
    # running（）#返回True当前正在执行无法取消
    # done（）#返回True如果调用成功取消或结束运行
    # result(timeout = None)返回调用返回的结果 ,如果调用未在超时时间内完成则报错
    # exception（timeout=None) 返回调用引发的异常。如果调用未完成，则此方法将等待超时秒。
    # add_done_callback（fn ） future对象的回调函数 ,当已取消或者已完成 就会调用这个传入的回调函数
    # 
######################## concurrent.future 模块对象
# ---  concurrent.futures.as_completed（fs，timeout = None ）
#     他和map() 差不多
#     他接收一个Future 对象 返回一个生成器
#     给他一个字典类型的键值对
#     而map()会把 参数顺序的传递给函数 执行的顺序不阻塞
#     5.0  # wait(fs,timeout = None, return_when=ALL_COMPLETED)方法可以让主线程阻塞等待子线程的完成
#    
    # 方法接收3个参数，等待的任务序列、超时时间以及等待条件
    # 他接收一个fs返回的Future 实例 
    # 返回一个两个元素的元祖
    # 第一个元素是已完成或者已取消的调用
    # 第二是没有完成的调用
    # return_when 默认等于ALL_COMPLETED 也就是等待所有调用的完成
    # FIRST_COMPLETED 当任何未来完成或取消时，该函数将返回。
    # FIRST_EXCEPTION 通过引发异常，任何未来完成后，函数将返回。如果没有未来引发异常则等同于 ALL_COMPLETED。
    # ALL_COMPLETED   所有期货结束或取消时，该功能将返回。