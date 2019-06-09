# 1.0 获得一个合法的用户输入的三位数
num = int(input("请输入一个三位数字: "))
if not(99 < num < 1000):
    exit()
# 2.0 判断是否是水仙花数
baiwei = num//100
shiwei = num%100//10
gewei = num%10
# 3.0 输出
result = (baiwei**3 + shiwei**3 + gewei**3 == num);
if result:
    print("您输入的%d是一个水仙花数" % num)
else:
    print("您输入的%d不是一个水仙花数" % num)