import random
num = random.randint(0,10)
index = 0
while index < 3:
    num1 = int(input("猜一个数字： "))
    index += 1
    if num1 > num:
        print("大了")
        print("您还有%d次机会" % (3-index))
        continue
    elif num1 < num:
        print("小了")
        print("您还有%d次机会" % (3-index))
        continue
    else:
        print("对了")
        break