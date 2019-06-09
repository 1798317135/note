# 上下文管理器 指的是，一个实现 __enter__（self）
# 1.0  with （上下文管理器）as 接收 __enter__方法 返回的值
# 2.0 执行 body 代码体
# 
# 3.0 最后执行 和__exit__（self,exc_type,exc_value,exc_tb) 方法
#     这个方法接收 四个参数 第一个所在类的实例化对象 
#     只要 body体 返回 异常 就会被__exit__接收，
#     exc_type 是 body代码体里面的 错误类型 
#     exc_value 是body代码体 里面 错误 的值 
#     exc_tb 是body 代码体 追踪错误对象       
#     如果这个方法 return 返回一个 True 则 这个方法接收到的 异常 会往外抛出 系统会报错
#     如果返回一个 False 接收到的异常信息 不会继续向外面传递 系统不会报错
#     
# --- 用 traceback 模块的
#       traceback.extract_tb()可以后去 追踪对象里面 的信息
import traceback
# class Context_manager:
#     def __enter__(self):
#         print("enter")
#         return 12   
#     def __exit__(self,exc_type,exc_value,ext_tb):
#         print(self,exc_type,exc_value,ext_tb)
#         print(traceback.extract_tb(ext_tb))
#         print("exit")

# with Context_manager() as c:
#     print(1 / 0)
#     print("body",c)

#####################################  快速生成上下文管理器 ##################################
#
# 1.0 需要导入 contextlib模块
# 
import contextlib

# --- @contextlib.contextmanger 可以把一个生成器快速 让其变成一个上下文管理器
#     从而达到 代码 和 异常铺货分离的目的
# 
# 1.0 如果让实现快速，创建一个上下文管理器械，需要用@contextlib.contextmanager
#     装饰一个生成器
# 2.0 生成器内部用 try: 这里自动执行 whith 语句 执行的代码块
#     except 捕获 代码块的 错误信息
#     
# 3.0 用 yield 可以返回一个 上下文管理器返回的一个对象
# 
# 4.0
@contextlib.contextmanager
def maker():
    try: 
        yield "你好"
    except Exception as e:
        print(e)
num = 1
num1 = 0
# num2 = num / num1

with maker() as x:
    print(x)
    print(num / num1)
print("\n*"*5)

# print(type(maker()))
# 
# --- contextlib.closing(thing) 可以将一个拥有 close()方法的类，
#      自动实现 __enter__ 和 __exit__两个方法
#     让其变成一个上下文管理器
#     并且每次调用这个对象，最后都会自动调用这个cloce()这个方法
#     并且这上下文管理器 会把这个对象返回出去

class Context:
    def close(self):
        print("资源释放")

    def run(self):
        print("跑")


with contextlib.closing(Context()) as x:
    with maker() as y:
        print(name)

