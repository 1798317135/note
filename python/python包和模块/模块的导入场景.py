# --- 1.0 局部导入
#         也就是说在 局部，命名空间里面导入模块
#         那么这个模块的命名空间 只在这个局部生效
def run():
    import 自定义模块.m2 as m
    print(m.age)
run()

# --- 2.0 覆盖导入
#         让我们导入的模块 和 优先级高的模块重名的时候
#         那么优先级高的模块会覆盖 优先及低的模块
#         我们需要 用 from 指定这个模块 是从哪个包里面导入
#         的就可以 避免这种覆盖

# --- 3.0 循环导入
#          当两个模块相互导入的时候 会引发循环导入
#          在设计中不要 使用循环导入
#          
# --- 4.0 可选导入
#          当我们在导入 第一没有的时候自动导入第二个
#          那么我们可以使用 try 语句 进行错误捕获
#          
#         

try:
    import 自定义模块.m4 as m
except Exception as e:
    import 自定义模块.m2 as m
print(m.name)

# --- 5.0 包内导入 
#         当包内 和包内的模块进行导入 使用的路径是相对路径
#         当包外 和包内的模块进行导入的时候，使用的是绝对路径
        
#         --在 3.0 x 之前 
#         我们在 包外 导入 包内模块的时候 会把 包的 根路径的绝对 路径 写入 sys.path
#         路径列表当中
        
#         于是 包内 在去导入 包内 的时候 无法在从 相对路径 找到 另外一个包内模块
        
#         所以 我们 可以使用 . 和 .. 来指定包内模块导入包内 的上级目录里面的 模块
#         和 包内 上上级别 目录的 模块
#         但是 如果越顶 了 也就是 你查找的目录已经到包的根目录 了 你还要往上层 查找
#         那么 就是报错
#         --- 3.0 x 以后 我们 不需要在使用 . 和 .. 来导入包内 上级目录里面 的模块
#         以为系统自动 会往上层 去查找 也就是 隐式的 相对目录 
#         那么为了 兼容 3.0 x 以前的版本，因为这种隐式的 相对路径 3.0x 之前并不能识别
#         所以 我们 需要禁用这种隐式的 相对路径，
#          from_futrue_import absolute_import 来禁用 隐式的相对路径 查找
#          我们可以手动的 用. 和 .. 来查找 相对模块的上级目录，或者上上级目录里面的模块
#          