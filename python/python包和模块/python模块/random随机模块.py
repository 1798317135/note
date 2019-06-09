import random

#random() 随机生成0-1之间的小数 可以取到0 但是取不到1
print(random.random())

# random.choice() 可以随机取出给定的列表
arr = [2,2,2]
print(random.choice(arr))

#random.uniform(x,y)可以随机取出,给定范围的随机小数 可以包括给定的范围界限 
print(random.uniform(1,9))

# random.randint(x,y)可以随机取出给定范围的整数 可以包括x 或者 y
print(random.randint(1,9))

# random.randrange(x,y,z) 随机取出给定范围的整数 包括x 不包括y z表示步长可以规定取出的是奇数 或则偶数
print(random.randrange(1,100))

# issubclass() 判断前面的类型是否是后面的子集
print(issubclass(bool,int))

print(True + 1)
# random.sample(population, k)随机取出
print(random.sample("asdfasdfasdf",6))

list = [1,2,3,4,5,6,7,8,9]
random.shuffle(list)
print(list)
