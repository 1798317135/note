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
# %n  存储输出字符的数量放进参数列表的下一个变量中
# 完整格式 []里面的可以省略
# %[(name)][flags][width][.precision]类型码(codetype)
# name查找传入参数 键[key]对应的值
# 
# 
# --------------------------- 1.0 example --------------------------------
# 
# 
name = "yang"
age = 18
print("我的名字是%s,我的年龄是%d"%(name,age))


 # -------------------- 2.0 example about %[(name)]的作用 -----------------
 # 
 # 
 # 
 # --- name表示传入字典的键【key】对应的value
mathScore = 50
englishScore = 45
print("我的数学成绩是%(mh)d,我的英语成绩是%(eng)d"%({"mh":mathScore,"eng":englishScore}))


# ---------------------- 3.0 example about %[flges]的作用 ------------------
# 
# 
# --- flges 表示站位是左对其还是右对齐
# 默认为空表示右对齐
# 
fe = "a";
print("%5s"%fe,"|右对齐")
# --- 左对齐 -号
print("%-5s" % fe,"|左对齐")
# --- 一个空格填充，多个无效，最多为一个空格 可以运用在 %s
num = 2
print("%02d:%-2s" %(num,fe),"|空格填充")
# --- 字符%s不能用空格补位 可以用widht宽度补位
print("%6s%06d" % ("abcd",123),"|补位")
# --- 0 表示用 0填充 以运用在%s
d = 1
m = 5
print("%04d:%04d" % (123,456),"|%d 0 补位")

# -------------------- 4.0 example about %[width]的作用 ---------------------
# 
# --- width表示站位的宽度包括自身的位数，如果小于自身则没有任何作用
aa = "abcd"
print("%5s" %aa,"|width");

# -------------------- 5.0 example about %[.precision]的作用 ----------------
# 
# .precision 可以给 %f取小数位置
# 
float = 19.123456
print("%d" % (float),"|%d float") #%d只去整数
print("%f" % (float),"|%f float") #%f取6位小数点
print("%.2f" % (float),"|%f float .2")#.precision就是规定%f的小数位的用.2表示

# -------------------- 6.0 example about %codetype的作用 ---------------------

num = 10
two = 0b1010

print("%x" % (num),"|%x 十六进制进制") #转换为十六进制的
print("%X" % (num),"|%X 十六进制进制大写字符") #转换为十六进制的大写字符
print("%o" % (num),"|%o 八进制") #转换为八进制
print("%c" % (100),"|%c ASCII转换") #把ascii转为字母
print("%g" % (1.0),"|%g 是什么类型就显示什么类型") #自动转换是float就显示float 是int就显示int
print("%g%%" %(69),"|%g%% 显示百分号")

# ############################## .fromat ######################################
# 
print("{}{}{}".format("aa","bb","aa"))

print("我的名字是：{name}{name}，我的年龄是：{age}".format(name = "yang",age = 18))

print("第一{0}第二{1}呵呵{aa}第三{num}".format(1,2,num = 12,aa= [1,2,3]))

import math
print("pi{}".format(math.pi))


print(("pi{0:.2f}".format(math.pi)))

print(("你哈{0:10}呵呵".format("呵呵")))

table = {'Google': 1, 'Runoob': 2, 'Taobao':"aa"}
print('Runoob: {Runoob}; Google: {Google}; Taobao: {Taobao}'.format(**table))


