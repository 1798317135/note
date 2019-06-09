# --- 栈遵循先进后出的原则
#       栈(Stack)是限制插入和删除操作只能在一个位置进行的表，
#       该位置是表的末端，称为栈的顶(top)。栈的基本操作有PUSH(入栈)和POP(出栈)。
#       栈又被称为LIFO(后入先出)表
class Stack:

    def judeg(fun):
        def inner(self):
            if self.stack == []:
                raise IndexError("stack is empty")
            else:
                return fun(self)
        return inner

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self,item):
        self.stack.extend(item)

    @judeg
    def pop(self):
        return self.stack.pop()

    @judeg
    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def __str__(self):
        print("这是一个栈")

# s = Stack()
# s.push([1,2,3])

# print(s.pop())
# print(s.pop())
# print(s.peek())
# 
# ---- 队列遵循先进先出的原则
#      queue模块有三种队列及构造函数:
#      Python queue模块的FIFO队列先进先出。 class queue.Queue(maxsize)
        # LIFO类似于堆，即先进后出。 class queue.LifoQueue(maxsize)  
        # 还有一种是优先级队列级别越低越先出来。 class queue.PriorityQueue(maxsize)
#       
# queue.qsize() 返回队列的大小
# queue.empty() 如果队列为空，返回True,反之False
# queue.full() 如果队列满了，返回True,反之False
# queue.full 与 maxsize 大小对应
# queue.get([block[, timeout]])获取队列，timeout等待时间
# queue.get_nowait() 相当queue.get(False) 他是非阻塞的
# queue.put(item) 写入队列，timeout等待时间
# queue.put_nowait(item) 相当queue.put(item, False) 他是非阻塞的
# queue.task_done() 在完成一项工作之后，queue.task_done()函数向任务已经完成的队列发送一个信号
# queue.join() 实际上意味着等到队列为空，再执行别的操作


