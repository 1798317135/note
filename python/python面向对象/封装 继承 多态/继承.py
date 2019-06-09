import inspect

# inspect.getmro() 可以查看 类的继承顺序 
# 
#  --- python的继承 大致分为三种 
#      也会存在错误继承
#      1.0 单继承形态
#          单继承是a 继承 b b 继承 c
#      2.0 无重叠的多继承形态
#           a 继承 b和 c  b继承e c继承d
#      3.0 有重叠的多继承形态
#           a 继承b 和 c b 和 c 继承 d
#      4.0 错误继承
#           a 继承b 和 c c继承 b b 继承d 
#  --- python的继承应该遵循重写可用的原则，和局部优先的原则
#       重写可用 原则是指 在两个子类 同时继承一个父类的时候 这两个的子类的优先级别 高于他们共同的父类
#       局部优先指的是  先左后右边
#           
#  --- pyton 每个版本的 继承算法不同 那么我们 就从早期的python版本 到最新版本的 演变
#       来学习 各种 继承算法 以及优缺点
#       
#      --- 2.2 x 以前 python 的类 只有经典类 他是通过MRO(翻译过来就是 继承顺序)算法
#           MRO算法秉持 深度优先的 原则
#           用 压栈的
#          来计算 类的继承顺序
#          深度优先 是只 从下而上 从左链优先的继承顺序
#          把 类 压栈弹出 每次弹出 都会检测 后面时候 还有父类 
#          但是 如果后面的父类 已经弹出 则不会继续压栈 后面的类
#      --- 但是这种算法 在运算 上述 第三种有重叠多继承形态的时候 会违背 重写可用的原则
#           他会把 共同的父类 的优先级 高于 右链的子类 违背了 重写可用的原则
#           
#      --- 从2.2x 往后python出现了新式类 也就是可以 继承 系统内部 object类 
#           这样的话 有重叠 多继承形态 这种菱形继承 就会很多 但是 深度优先的 原则 已经
#           无法 运算这种形态的 继承顺序，所以在2.2版本以后 出现了 类似度优先原则 的算法
#           类似广度优先 只是 在深度优 原则算法上 进行改进
#           类似广度优先 仍然使用 压栈 的方法 进行排序 当遇到 共同 的父类时候 仍然进行深度优先的原则
#           但是 会把后面的父类全部压栈 无论前面是否已经存在
#           但是深度优先 会在 最后排序的结果 检测从重复 类 并且 后面的类会覆盖前面的相同的类
#           这样计算的结果 顺序就不会违背 重写可用的 原则
#         - 但是 类似广度优先的算法并不能 识别 上述 错误继承 会违背先左后右的 局部优先原则
#       
#      --- 3.0 新式类 全部采用 c3 算法
#           c3 算法 可以解决上述全部的问题
#           L(object) = [object]
#           l[子类(父类1,父类2)] = [子类]+marge(L(父类1)，l(父类2)，[父类1，父类2])
#           但是 c3 算法 可以识别 错误继承并且报错 ，还有一种算法 可以 算出
#           这种错误的继承 并且不会报错 那就是 拓扑排序方法
#           
#      --- 拓扑排序 方法 首先会找到 入度为0的类 也就是他继承了其他类，没有类继承他 也就是入度为0
#          找到后 删除他继承 其他类的指针 把他排序到第一位
#          然后 在网上找入度为 0 的类 删除他指向其他类的指针 然后排序到第二位 
#          依此这样 就可以 得到最后的排序 也就是 继承优先级 

# ---- 菱形 继承形态
# class D: 
#     pass
# # L(D(object)) = [D] + marge(L(object),[object]) 
# #                [D,object]
# class C(D):
#     pass
# # L(C(D,object)) = [C] + marge(L(D),L(object),[D,object])
# #                  [C] + marge([D,object],[object][D,object])
# #                  [C,D]+marge([obect],[object],[object])
# #                  [C,D,object]
# class B(D):
#     pass
# # L(B(D,object)) = [B] + marge(L(D),L(object),[D,object])
# #                  [B] + marge([D,object],[object][D,object])
# #                  [B,D]+marge([obect],[object],[object])
# #                  [B,D,object]
# class A(B,C):
#     pass
# #  L(A(B,C,object)) = [A] + marge([B,D,object],[C,D,object][B,C,object])
# #                     [A,B,C,D,OBJE]
# print(inspect.getmro(A))

# ---- 错误继承形态 
# 

class B:
    pass
# 1.0 用 L 函数 计算 B的自身 和 父类的继承 顺序 然后让自己组成一个列表 加上
#     marge()函数 用L()函数计算父类的 继承顺序，后面 让父类生成一个列表
#     
# L(B(Object))  =  [B] + marge(L(object)，[object])
# 
# 2.0 计算 出 marge函数里面 计数出来的所有父类 生成列表  
# 
#                  [B] + marge([object],[object])
# 3.0 判断 marge函数里面 第一个 父类生成 的列表 的第一个元素，检索后面的 列表
#      第一个元素是否与这个第一个列表的 第一个元素相等 
#      如果有相等 那就推入子类的列表
#      这样依此 检索到 后面的 父类列表 为空
#      然后会继续 网下一个子类里面计算
#                  [B,object]       
class C(B):
    pass
# L(C(B,object)) = [C] + marge(L(B),L(object),[B,object])
#                  [C] + marge([B,object],[object][B.object])
#                  [C,B] + marge([object],[object],[object])
#                  [C,B,object]
class A(B,C):
    pass
# L(A(B,C,objcet)) = [A] + marge(L(B),l(C),L(object),[B,C,object])
#                    [A] + marge([B,object] ,[C,B,object],[[B,C,object]])
#                    [A,B] + marge([object],[C,B,object],[C,object])
#                    [A,B,C] + marge([object],[B,object],[objcet])
#                    [A,B,C,objcet] + marge([b])
#                    不能解析 报错
#                    
# print(inspect.getmro(A))
# print(A.__mro__)