# --- 单例设计模式就是一个对象用永远只有一个实例对象
# 1.0 回收站，音乐播放，等等可以运用单例模式
# 2.0 实现单例模式可以对__new__方法进行重写，从而控制每一次返回的对象引用地址都是相同的
#     从而达到单例模式，即每个对象只有一个实例
# 3.0 然后限制多次的实例初始化动作，从而只在实例化的第一次执行初始化动作，往后的创建不执行初始化动作

class MusicPlayer:

#   定义一个储存第一次创建的实例的引用地址的类属性
    __instance = None
#   定义一个第一次初始化动作的变量
    __flag = False

    def __new__(cls,*args,**kwargs):
        # 判断是否为None 如果为None就是第一次创建实例，直接返回这个实例
        if cls.__instance is None:
            cls.__instance = super(MusicPlayer,cls).__new__(cls,*args,**kwargs)
            return cls.__instance
        # 这里返回的都是第一次创建的同一个实例
        return cls.__instance

    def __init__(self):
        #判断是否是一个次初始化动作
        if MusicPlayer.__flag is False:
            print("音乐播放器初始化")
            MusicPlayer.__flag = True


m = MusicPlayer()
m1 = MusicPlayer()
print(m is m1)
print(m)
print(m1)