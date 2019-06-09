
# ****************************************  字典的定义(dict) ************************************
# 
# 1.0  python的字典(dict)，类似于javascript(object)里面的对象，由键值对组成
# 2.0 字典是无序的，可变的元素集合
# 
# ********* python中 定义字典的方式一  ***********

person = {"name":"yang","age":18,"sex":"男"}
print(type(person))

# --- 可以通过每个元素的建 来取出对应的值
# 
print(person["name"],"name")
print(person["age"],"age")
print(person["sex"],"sex")

# ************  定义的方式二 通过静态方法定义 ***********
# 
# --- dict.fromkeys(iterable, value) 用可迭代的对象的每个元素作为键,value为每个键对应的值
# 如果没有这只value，那么每个键的值为none
# 
dic = dict.fromkeys("123", 666)
print(dic) #{'1': 666, '2': 666, '3': 666}

# *******定义方式三，用实例对象进行定义 但是通常不会用这种形式，进行定义字典（dict）*******
# 
dic  = {}.fromkeys("123",666)
print(dic) #{'1': 666, '2': 666, '3': 666}

# ######################################  注意点 #######################################
# 
# 
# --- 1.0 字典的key 是不能重复的 如果重复出现相等的key ，
# 那么后面的值会覆盖前面的值 但是位置还是第一个出现的位置
# 
dic = {"aa":1,"bb":2,"cc":3,"dd":4,"aa":"yang"}
print(dic)

# --- 2.0 字典的key必须是一个不可变的值 不可变是指 值在内存中的 id是固定的没有重复的
# id 可变的有 列表 字典 可变集合
# id 不可变的有 数值 字符串 元组 布尔

# #################################### 字典操作 #######################################
# 
dic = {"name":"bruce","age":18,"sex":"男"}
print(dic)
# ******************* 曾   **********************
# 
# 1.0 如果存在则会修改
# 2.0 如果不存在则会增加
# 
a = dic["height"] = 180
print(a)
print(dic,"add")

# ******************** 删  **********************
# 
# --- del删除已经存在的键值对 如果不存在则会报错 KeyError:
# 
del dic["age"]
print(dic,"del")

# --- dict.pop(key，[default])
# 
#  删除已存在 key对应的值 并返回删除的值 
#  可以指定默认返回的值如果删除的key 不存在则返回默认设置的值返回

d = dic.pop("name1",666)
print(d)
print(dic,"pop()")

# --- dic.popitem() 没有参数 先会把字典进行升序排序 
# 然后删除排序后第一个值 并以元组的形式返回
# 
obj = {"dd":11,"bb":12,"cc":13,"aa":14}
d = obj.popitem()
print(d)
print(obj,"popitem()")

# ---obj.clear() 没有参数 返回值为none 直接清空字典 但是字典仍然存在 只是没有内容了
# 用del 删除字典名 才能完全删除字典
c = obj.clear()
print(c)
print(obj,"clear()")
print(dic)
# del 字典名 直接删除整个字典
del dic

# ******************** 改 *********************
# 
# 1.0 只是修改值 而不会修改key
# 2.0 如果增加的key存在就是修改 如果不存在就是删除
# 
dic = {"name":"yang"}
dic1 = {"name":"猪","age":18,"height":180}
dic["age"] = 19
print(dic) 
dic["name"]="猪"
print(dic,"dic")

# ---olddict.update(newdict)批量修改和覆盖，增加 如果没有的会增加 如果有的会覆盖新旧的值
# 
dic.update(dic1)
print(dic1,"dic1")
print(dic,"dic")

# ************** 查寻 ***************
# 
# 单个查询 dic[key] 这种方法如果没有则会报错
dic = {"aa":11,"bb":22,"cc":33,"dd":44}
print(dic["aa"])

# ---dic.get(k[,d])这个方法如果没有查到则返回none如果规定了返回值则返回规定的返回值
get = dic.get("ff",666)
print(get)

# ---dic.setdefault(k, d)
# 这个方法如果没有查询到 则会把没有查询到这个key 插入到字典当中 value为 none 
# 如果设置了么默认值则会把值 设置为默认值
st = dic.setdefault("ff",666)
print(st)
print(dic)

# --- 获取所有的值 dict.values()
vs = dic.values()
# --- 获取所有的键 dict.keys()
ks = dic.keys()
# --- 获取所有的键值对dict.items()
its = dic.items()
dic["aa"] = 10
# --- 上面返回的是一个Dictionary.view.object字典视图对象
# --- 他的原理就是 当字典发生改变的时候他的值也会跟着发生改变
# 
print(vs,ks,its)
print(list(vs),list(ks),list(its),end = "\n")

# **************** 字典的遍历  ****************
# 
# --- 直接或者值或者键 来进行遍历
# 
dic = {"name":"yang","age":18,"address":"上海"}
vs = dic.values()
dic["name"] = "朱"
for x in vs:
    print(x)
# 通过获取键值 然后解包遍历
its = dic.items()
for idx,val in its:
    print(idx+":",val)

# **************** 字典的判定 ****************
# 用len可以检测字典的长度

print(len(dic),"len()")

# 用in 或者 not in 来判定 检测的key 是否存在
# 
print("name" in dic) #True
print("name" not in dic) #False