# ############################# 列表的定义 和创建 ###############################
# 
# 
# 1.0 列表list 和 javascript里面的数组array差不多, 
# 2.0 是元素有序的集合
# 3.0 range([start],stop[,step])快速生成有序的列表 用的时候可以提取
arr = range(0,101)
print(arr[0],arr[100],"range(0,101)")
# 4.0 列表可以储存多种数据类型
# 
arr1 = [1,2,3,4,56,"asdf",True]

# 5.0 列表的映射解析 是一对一的解析,不会改变列表元素的个数
# 
# 6.0 列表过滤是删除列表指定的元素，返回新的列表
# 7.0 用list()内置函数可以将可迭代对象转换为列表
str = "asdf123"

print(list(str),"list()")

# 8.0 原始方式
arr = [1,2,3,4,5,6,7,8,9]
# --- 求出列表中所有的奇数

result = []
for x in arr:
    if x%2 == 0:
        continue
    result.append(x)
print(result)

# --- 列表推导式 更加方便
# --- 第一个可以写表达式 第二个可以是并且可以嵌套 第三个可以是判断语句
# 
listResult = [num for num in arr if num%2 == 0]
print(listResult,"列表推导式")


# ######################## 列表的常用操作 曾 删 改 查 ############################
# 
# ********************* 曾 ******************
# 
arr = [0,1,2,3,4,5,6]

# --- arr.append(object) 向列表末尾追加元素 
arr.append(7)
print(arr,"append()")

# --- arr.insert(index, object)在某个索引之前插入元素 返回一个none
arr.insert(1,2)
print(arr,"insert()")

# --- arr.extend(iterable)在列表尾部扩展一个可迭代对象 可以合并列表
# 
arr2 = {"name":"yang","age":18}
arr.extend(arr2)
print(arr,"extend()")

# --- 列表的乘法运算 在列表中指定重复插入的次数
 
print(arr*2,"列表的乘法运算")

# 列表的加法运算+ 只能合并两个list 从而创建一个新的列表 而extand()是扩展到指定列表中的可以迭代的对象
arr = [1,2,3,4,5,6]
arr2 = ["a","b","c","d"]
print(arr+arr2,"列表的加法运算")

# ***************  删除  *************
# 
# --- del list[index] 可以删除变量 和 列表
# 
arr = [12,24,5,63,1523]
print(arr)
del arr[-1]
print(arr,"del")
num = 152

# arr.pop([index])默认-1 删除列表最后一个元素 并返回它 如果可以自己设置需要删除的index
result = arr.pop(-1)
print(result,arr,"pop()") 

# arr.remove(value) 删除列表中指定的元素 如果没有会报错 默认删除的是索引为0的 元素
print(arr.remove(12),"remove()")


# ******************* 修改 *****************
# 
arr =  ["bb",1,2,3,4,5,6,7,"aa"]
arr[0] = "aa"
arr[-1] = "bb"
print(arr)

# ******************* 查询 ******************
#
# --- 查询单个元素的值 直接用这个元素的下标进行查询
# 
items = [1,2,3,2,4,5,6,7]
print(items)
print(items[0],items[1],items[-1],items[-2])

# --- items.index(value, start, stop)可以查询规定半闭合区间内的某个值的下标
idx = items.index(2,0)
print(idx,"index()")

# --- items.count(value)获取元素出现的次数
cot = items.count(2)
print(cot,"count()")

# --- 列表的切片操作 和 字符串的切片操作差不多
# 
print(items)
print(items[::1])
print(items[::-1])


# ############################## 列表的遍历 #################################
# 
# 
items = [1,2,3,2,4,5,6,7]
print(items)

# --- 遍历的第一种方式手动设置下标 每次循环让下标自增的方法全部遍历

current = 0
for x in items:
    print(x)
    print(items.index(x,current))
    current += 1

# --- 遍历的第二种方式用range(len(list))的方式动态生成下标 更为方便

for i in range(len(items)):
    print(items[i])

# --- 遍历枚举对象
# enumerate(iterable[, start])可以可迭代对象转换为枚举对象可选参数可以规定开始的下标
print(list(enumerate(items)))

# --- 设置的枚举对象可以自己规定下标从几开始
tup = list(enumerate(items,1))

# --- 用解包的方式解开枚举对象里面的每个包
# 
for idx,val in tup:
    print(idx) #第一个是下标
    print(val) #第二个是每个下标对应的值

# --- 转成迭代器后遍历 这种方式最为高效率

print(arr)
# iter(collection) 可以采集所有的可迭代对象把他们转为迭代器 iterator
it = iter(arr)
print(type(it))
print(next(it),"next()")
for i in it:
    print(i,"i")


# ################################  列表的额外操作 ############################
# 
# ************  1.0 判定   *************
arr = ["a",1,3]
print(1 in arr,"判定 in")
print(1 not in arr,"判定 not in")

# *************  2.0 比较 **************
# 比较每个元素的第一个
arr1 = [1,2,3,4]
arr2 = [2,3,4]
print(arr1 == arr2,"比较 ==")
print(arr1 > arr2,"比较 >") 
print(arr1 < arr2,"比较 <")

# *************** 3.0 排序 *************
# 
num = "asdfasdf456"
num = list(enumerate(num,0))
# --- sorted(iterable,key, reverse)
# 是一个内建函数 可以对所有的可迭代对象进行排序
# 第一个参数的可以迭代的对象 ，key = 一个可以返回每个元素比比对置的函数  reverse = Falst 默认正序
# 返回一个列表
# 不会改变原来的可迭代对象

print(num)
def getkey(x):
    # 返回枚举对象，每个元祖中第一个值作比对
    return x[1]
print(sorted(num,key = getkey, reverse = False))
print(num)

# --- num.sort(key, reverse)
# 是列表对象方法
# 和sorted()用法差不多 这个只能对列表进行排序
# 参数key，和reverse同上
# 他会直接该表原数组 返回none 空值
arr = [(1,5),(2,4),(3,3),(4,2),(5,1)]
print(arr)
def getkey(x):
    return x[1]
result = arr.sort(key = getkey,reverse = True)
print(result)
print(arr)

# ************************* 列表的乱序 和 翻转 ********************************
# 
import random
arr = [1,2,3,4,5,6,74,8]

# --- random.shuffle(arr)随机打乱列表 返回none空值
# 
l = random.shuffle(arr)
print(l, arr)


# --- 翻转列表本身用reverse() 返回none 
# 
arr = ["<",3,"aa",2,"|"]
r = arr.reverse()
print(r,arr,"reverse()")

# --- 翻转不改变列表本身可以用切片的方法
result = arr[::-1] 
print(result) 
print(arr)

# ************************ 列表的复制 *************************
l = [1,2,3,4,5,["aa","bb"]]
copy = l.copy()
print(l,id(l))
print(copy,id(copy))
print(l[5],id(l[5]))
print(copy[5],id(copy[5]))
# print(deepcopy)