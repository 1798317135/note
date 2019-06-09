from time import sleep
# print(
#   输出的顺序是 先读取字符，然后储存到缓存，然后在打印到控制台或者文档等等
#   1.0 value 值多个可以用,识别 ,
#   2.0 sep打印出来的效果分割符号 , 
#   3.0 end 输出完毕之后以指定符号结束，默认是\n换行,
#   4.0 file 表示输出的目标，默认是控制台输出，还可以是写入文件句柄
#   5.0 flush 是否缓冲输出 如果为true 直接输出不需要缓冲
# )

# 1.0 输出一个值
print(123);

# 2.0 输出一个变量
num = 11;
num1 = 22;
print(num,num1); 

# 3.0 格式化输出 
# python常用占位符 %f浮点数 %d整数 %s字符串 %x十六进制整数
name = "yang";
age = 18;
print("我的名字是%s,我的年龄是%d"%(name,age));

# 第二种方法 通过{inidex}下标的方式站位 用.format()进行填充
# 填充的顺序对从0开始对应的下标开始填充
print("我的名字是{0},我的年龄是{1}".format(name,age));

# 4.0 输出到文件当中

# 先通过open()打开一个文件如果不存在就自动创建一个规定的文件，
f = open("./text/print.txt","w");
# 通过file 方法把value写入打开的文件当中去
print("print.txt",file = f);

# 5.0 end表示结束符号
print(1,2,3,4,end = "结束");

# 6.0 flush 如果设置为True就不经过缓存直接输出到控制台

print("xxxx",end ="--",flush = True)

sleep(5);
