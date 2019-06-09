#############################################  集合的定义 ##################################
#
#1.0 集合(set) 是无序的,没有重复的,不可随机访问的可迭代对象
#
#集合 有两种 可变集合 和不 可变集合
#
#************** 可变集合set ******************
#
# --- 直接花括号里面放入值逗号隔开
st = {1,2,3,4,5,6}
print(type(st))

# --- set(iterable)将一个可迭代对象转为set集合
# 
# 1.0 如果是dict字典的话，会把每个键值对的值转换
print(set("abcd"),"字符串")
print(set([1,2,3,4]),"列表")
print(set((1,2,3,4)),"tuple元组")
print(set({"name":"yang","age":18}),"dict字典")
print(set(enumerate(st, 0)),"媒介对象")
print(set(iter(st)),"迭代器")
# --- 集合推导式 和 列表推导式差不多
print(set(num ** 2 for num in st if num%2==0))
#
#************** 不可变集合 frozenset****************
#
# 不可变集合的定义不能用{} 直接定义 需要用到frozenset(iterable)函数进行定义
# --- frozenset(iterable)
# 
print(frozenset("abcd"),"字符串")
print(frozenset([1,2,3,4]),"列表")
print(frozenset((1,2,3,4)),"tuple元组")
print(frozenset({"name":"yang","age":18}),"dict字典")
print(frozenset(enumerate(st, 0)),"媒介对象")
print(frozenset(iter(st)),"迭代器")
# --- frozenset()集合推导式
print(frozenset(num for num in range(0,11) if num % 2 == 0),"集合推导式")

############################################# 注意事项 ######################################
#
# --- 1.0在定义一个空集合的时候不能使用{} 这样会被识别成一个空空字典dect
print(type({}),"{}")

# --- 2.0 如果定义一个空的集合 要用set() 或者 frozenset()
print(set(),"set()")
print(frozenset(),"formzenset()")

# --- 3.0 集合里面的元素必须是一个可hash哈希的值 也就是不可变的值 不可变是 id在地址是独有的 不可重复的
# 
print(type({1,2,3,4,5,"aa",True}))

# --- 4.0 集合的元素不会重复的 如果重复则会合并 利用集合不可重复的特性 可以为列表去重操作
# 
print({1,2,2,3,4,5,6,52,2,2,2,2}) 

arr = [1,2,2,2,3,3,4,5,6,7,8,8,9,8,8,9]
result = set(arr)
l = list(result)
print(l)

############################################## 集合的常用操作 ##################################
#
st = {1,2,3,4,5,6}
print(st)

#************** 单一集合操作 **************
#
#1.0 不可变的集合frozenset() 不能进行曾删除改
#
# ------ 曾 ------
# 
# --- set.add() 在后面增加一个元素
# 
st.add("aa")
print(st,"add()")

# ------ 删 ------
# 
# --- del 删除整个集合
del st

# ---remove() 删除指定元素 如果没有则会报错  和list对象的remover() 类似
st = {1,2,3,4,5}
st.remove(1)
print(st,"remove()")

# st.discard() 删除指定元素 如果没有 则do nothing 不做任何处理
st.discard("aa")
print(st,"discard()")

# st.pop() 随机删除一个元素,并且返回删除的元素，如果删除空的集合则会 报错
print(st.pop())
print(st,"pop()")

# st.clear() 清空集合 并不是删除是清空内容 
st.clear()
print(st,"clear")

# ------ 改 ------
# 
# --- 集合set 是不可修改的
# 
# ------ 查 ------
# 
# --- 集合是不可随机访问的 所以集合不能用key 查询
# 
# ************* 集合的遍历 ****************
# 
# --- for in 进行遍历
del st 
st = {1,2,3,4,5,6}
ft = frozenset({1,2,3,4,5,6,7})
for x in ft:
    print(x,"for in")

# --- iter()转换为迭代器 进行遍历
st = iter(st)
ft = iter(ft)
for i in ft:
     print(i,"iter()")
del st,ft

#
#************** 集合之间的操作 *************
#
st = {1,2,3,4,5,6,7,8}
ft = frozenset({7,8,9,10})
str = "123456"
list = [1,2,3,4,5,6,7]
tuple = (1,2,3,4,5,6,7)
dict = {1:5,2:4,5:3,6:2,7:1}
#------- 交集 -------
#
#1.0 谁在前面 得出交集的值就是什么类型
#2.0 a 交 b 交集指的是 a 和 b 相交的那一部分
#
# --- st.intersection(other)交集
# other是一个可迭代的对象 
# 如果是字符串 则需要集合的元素也是字符串类型 否则为空
# 如果是一个字典 则会拿字典的键(key)进行对比
# 
result = st.intersection(tuple)
print(result,type(result),"intersection()")

# --- & and 逻辑符 获得交集部分 这种方式只支持 集合 set（） 和forzenset（）
result = ft & st
print(result,"&")

# --- st.intersection_update(iterable) 
# 可以是一个可迭代的对象
# 这中方式只支持 set（）
# 他会删除没有并集的元素 保留交集的元素
# 返回的是 none空
# 
print(st)
result = st.intersection_update(ft)
print(result,type(result),"intersection_update()")
print(st,ft)
#------- 并集 -------
#
#1.0 集合的并集和交集类似 谁在前 得出的结果就是什么类型
#2.0 a 并 b 并集指的是 a 和 b合并
#
st = {1,2,3,4,5}
ft = frozenset({4,5,6,7,8})

# --- union(iterable) 
# 如果是字符串 则需要集合的元素也是字符串类型 否则为空
# 如果是一个字典 则会拿字典的键(key)进行对比
# 
result = st.union()
print(result,type(result),"union()")  

# ---  逻辑或 | 
result = ft | st
print(result,type(result),"|") 

# --- update(iterable)并集 
# 值是一个可迭代的对象 
# 并且把对象的内容改为并集内容
# 支持可变的集合set 不支持不可变的集合frozenset
# 返回的是空值none

print(st)
result = st.update(tuple)
print(result,type(result),"update()")
print(st,tuple)

#------ 差集 -------
#
st = {1,2,3,4,5}
ft = frozenset({4,5,6,7,8})

# 1.0 跟交集和并集 操作类似 非常类似 谁在前最后的类型就是谁
# 2.0 a 差 b ，差集指的是 属于a的不属于b的那一部分
# 
# --- st.difference(iterable)
# 可以是一个可迭代的对象
result = ft.difference(st)
print(result,type(result),"difference()")

# --- -号 
result = st - ft
print(result,type(result),"-")

# --- difference_update(iterable)
# self 只支持set 可变集合
# other 可以是可迭代的对象
# 修改结果 值就是差集
# 返回空none 
result = st.difference_update(ft)
print(st,ft,"difference_update()")
#------判定 --------
#
st = {1,2,3,4}
ft = frozenset({5,6,7,8})
str = "1234"
list = [1,2,3,4,5,6]
tuple = (5,6)
dict = {1:"aa",2:"bb",3:"cc"}
# st.isdisjoint() 判断两个集合是否不相交
print(st.isdisjoint(ft))
# st.issubset() 判断一个集合是否包含于另一个集合
print(st.issubset(list)) 
# st.issuperset() 判断一个集合是包含另一个集合
print(st.issuperset(dict))
#
#
#************** 注意点 ********************

