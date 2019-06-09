# %%  百分号标记
# %c  字符及其ASCII码
# %s  字符串
# %d  有符号整数(十进制)
# %u  无符号整数(十进制)
# %o  无符号整数(八进制)
# %x  无符号整数(十六进制)
# %X  无符号整数(十六进制大写字符)
# %e  浮点数字(科学计数法)
# %E  浮点数字(科学计数法，用E代替e)
# %f  浮点数字(用小数点符号)
# %g  浮点数字(根据值的大小采用%e或%f)
# %G  浮点数字(类似于%g)
# %p  指针(用十六进制打印值的内存地址)
# %n
# 完整格式 []里面的可以省略
# %[(name)][flags][width][.precision]类型码(codetype)
# name查找传入参数 键[key]对应的值
# 
# 
# -------------------- 1.0 example -----------------
# 
name = "yang"
age = 18
print("我的名字是%s,我的年龄是%d"%(name,age))

 # -------------------- 2.0 example about %[(name)]的作用 -----------------
 # 
 # name表示传入字典的键【key】对应的value
mathScore = 50
englishScore = 45
print("我的数学成绩是%(mh)d,我的英语成绩是%(eng)d"%({"mh":mathScore,"eng":englishScore}))

# -------------------- 3.0 example about %[flges]的作用 -----------------
# flges 表示站位是左对其还是右对齐
# 默认为空表示右对齐
fe = "aaa";
print("%5s" % fe)
# - 左对齐
print("%-5s" % fe)
# 一个空格，多个无效最多为一个空格 可以运用在%s
num = 2
print("%02d:%-5s" %(num,fe))
# 字符%d不能用空格补位 可以用widht宽度补位
print("%-5s" % fe)
# 0 表示用0填充 以运用在%s
d = 1
m = 5
print("%02d:%0-2d" %(d,m))

# -------------------- 4.0 example about %[width]的作用 -----------------
# width表示站位的宽度包括自身的位数，如果小于自身则没有任何作用
aa = "abcd"
print("%5s" %aa);

# -------------------- 5.0 example about %[.precision]的作用 -----------------
# .precision 可以给 %f取小数位置
float = 19.55
print("%d" % (float)) #%d只去整数
print("%f" % (float)) #%f取6位小数点
print("%.2f" % (float))#.precision就是规定%f的小数位的用.2表示

# -------------------- 6.0 example about %codetype的作用 -----------------

num = 10
two = 0b1010

print("%x" % (num)) #转换为八进制的
print("%g" % (1.0)) #自动转换是float就显示float 是int就显示int
print("%g%%" %(696))

# ------------------- 7.0 str.formate格式化输出 --------------------------------
# str.formate 是为了代替 % 的更加强大的字符格式化输出
# --- 不指定位置,默认是按照顺序来的
print("{}{}".format(123,456))

# --- 指定顺序
print("{0}{1}".format(456,123))
print("{0}{1}{0}".format(123,456,123))

# --- 设置参数
name = "Bruce Lee"
age = 32
print("我的名字是:{name},我的年龄是:{age}。".format(name = name,age = age))

# --- 通过字典方式传递参数需要解包字典
dict = {"name":"Bruce Lee","age":18}
print("我的名字是:{name},我的年龄是:{age}".format(**dict))

# --- 通过索引的方式传参 "0" 是必须的
list = [1,2,3,4,5]
print("{0[0]}+{0[1]}={0[2]}".format(list))

# --- 传入对象  "0" 是必须的
class Name():
    def __init__(self,name):
        self.name = name

name = Name("Bruce Lee")
print("名字是:{0.name}".format(name))

# --- str.format()格式化数字的多种方法
# 1.0 {:.2f} 是保留小数点后面几位 类似 %.2f
print("{:.2f}".format(1.11111))

# 2.0 {:+.2f} 带符号的保留小数点后几位 只能是正号+ 或者符号-  
print("{:+.2f}".format(3.141592654))

# 3.0 不带小数 类似 %
print("{:.0f}".format(3.145))

# 4.0 设置数字宽度 超过的宽度默认是用空格填充在左边
print("{:5d}".format(10))

# 5.0 用0填充左边宽度为3
print("{:0>3d}".format(5))

# 6.0 用*符号填充在右边 宽度为3
print("{:*<3}".format(2))
print("{:x<3}".format(10))

# 7.0 以逗号分隔数字
print("{:,}".format(30000000))

# 8.0 百分比
print("{:.0%}".format(3)) 

# 9.0 左对齐
print("{:0>5}".format(3))

# 10 右对齐
print("{:0<5}".format(3))

# 11 居中对齐
print("{:0^5}".format(3))

# 12 格式化符号
print("{:d}".format(1))
print("{:.0f}".format(32))
print("{:#x}".format(10))
print("{:c}".format(333))
print("{:g}".format(123))
print("{:s}".format("你好"))
print("{:b}".format(123))
name = {0:"name"}