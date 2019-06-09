# 1.0迭代是访问集合元素的一种方式 
# 
# 2.0 迭代可以按照某种顺序来依此访问可迭代对象
# 
# 3.0 可以被迭代的对象叫做可迭代对象
# 
# 验证是否是可迭代对象的方法 1.0 用for in 语句看是否可以遍历 
num = "abc"
boo = True #这个就不能遍历 所有就不是可迭代对象
arr = [1,2,3,54,"aa"]
tup = (1,2,3,4,5)
obj = {1,2,3,45}
for x in obj:
    print(x)

# 验证的方法二 通过 判定是否是可迭代对象
# isinstance(obj, class_or_tuple) obj 需要验证的对象 第二个参数验证的方法
# 
import collections

# str是否可迭代  True
print(isinstance(arr,collections.Iterable)) 

# 元祖是一个可迭代的对象
print(isinstance(tup,collections.Iterable)) 

 #True 不是一个可迭代的对象
print(isinstance(boo,collections.Iterable))

# 迭代器 
# 1.0 迭代器是一个记录遍历的对象
# 2.0 用next()从第一个往后面开始迭代 每次调用next()都会记录位置
# 3.0 只能往后不能往前
# 4.0 用iter()可以生成后者把迭代对象转换为迭代器
# 5.0 迭代器本事就是可迭代对象
# 6.0 迭代器犹豫 在指针迭代到的前后都会销毁指针，所以性能比较好
# 7.0 可以把所有可迭代对象用iter()转为迭代器后迭代 ，增加性能，统一遍历方式
# 8.0 可以用for in 遍历迭代器 但是每个迭代器只能得带

arr = [1,2,23,"aa"]
it = iter(arr)
print(it)
# 用isinstance() 可以验证是否是一个迭代器
isinstance(it,collections.Iterator)
# 或者可以用next()验证 如果不是则报错
print(next(it),"next()")
# 如果超出迭代对象 会报错 StopIteration
# 迭代器就是一个可迭代对象
print(isinstance(it,collections.Iterable))
for i in it:
    print(i)