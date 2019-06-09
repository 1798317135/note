# ################## 99 乘法表 ###########################
# for num in range(1,10):
#     nums = range(1,num+1)
#     for n in nums:
#         print("{0} * {1} = {2}".format(n,num,n*num),end = "\t")
#     print("")

##################### 水仙花数 ###########################
# while True:
#     try:
#         num = input("请输出一个三位数的数值:")
#         num = int(num)
#     except Exception as e:
#         print("请重新输入一个输入一个数值类型！")
#         continue
#     else:
#         gewei = num % 100 % 10
#         shiwei = num % 100 // 10
#         baiwei = num //100
#         if len(str(num)) != 3:
#             print("请重新输入一个三位数值!")
#             continue
#         elif gewei**3 + shiwei**3 + baiwei**3 == num:
#             print("{}是一个水仙花数".format(num))
#             break
#         else:
#             print("{}不是水仙花数".format(num))
#             continue

######################## 猜数字 ##############################
# import random
# result = random.randint(0,10)
# index = 3
# while True:
#     index -= 1
#     try:
#         num = input("请猜数字您剩下{}次机会!:".format(index+1))
#         num = int(num)
#     except Exception as e:
#         if index<=0:
#             print("你没有机会了,自动退出")
#             break
#         else:
#           print("请重新输入数值类型,还有{}次机会!".format(index))
#           continue
#     else:
#         if index <= 0 and num != result:
#             print("机会用完了")
#             break
#         else:
#             if num > result:
#                 print("太大了")
#                 continue
#             elif num < result:
#                 print("太小了")
#                 continue
#             else:
#                 print("恭喜你猜对了！")
#                 break
######################### 数值 ###########################
# print(bin(12))
# print(oct(12))
# print(hex(12))
# print("nihao","sdf",end = "",sep = "--", file = open("复习.text","w"))
# print(chr(125))
# #################### 常用函数 ##########################
# print(abs(-123))
# print(min(1,2,3))
# print(max(4,5,6))
# print(round(2.5)) 
# print(pow(2,4),2**4)
# import math
# print(math.ceil(3.1))
# print(math.floor(3.9))
# print(math.sqrt(9))
# print(math.log(2))
# import random
# print(isinstance(12,float))
# print(random.sample("sdfsdfsdf",1))
# list = [1,5,6,6,52,3,12,4,7]
# random.shuffle(list)
# print(list)
####################### 字符串 ###########################
# print(type("123"))
# print(type('sdf'),type("""456"""),type('''789'''))
# print(r"sdf\nsdf")
# print("ran\nsdf")
# print(r'''sadf\nsdf54\\s465''')
# print("")
# str = "hellow words"
# str = "ABCD"
# print(str.find("s",3,7))
# print(str.index("s",0, 5))
# print(str.replace("s","是",2))
# print(str.capitalize())
# print(str.title())
# print(str.lower())
# print(str.upper())
# str = " abc def "
# print(str.ljust(8,"."))
# print(str)
# print(str.rjust(8,"x"))
# print(str.center(9,"x"))
# print("|"+str.lstrip(" a")+"|")
# print("|"+str.rstrip(" f")+"|")
# str = ["name","age"]
# ls= "-"
# print(ls.join(str))
# print(str.split("-",1))
# print(str.partition("-"))
# print(str.rpartition("-"))
# print(str.splitlines(False))
# print(str.join("|||||||"))
# print(str.startswith("sz-18-aa"))
# str = "abcd"
# num = "\n\t "
# print(str.isalpha())
# print(num.isdigit())
# print(num.isalnum())
# print(str.isalnum())
# print(num.isspace())
# print(str.startswith("bc",1,3))
# str = "aa.text"
# print(str.endswith(".text"))
# str = "abc"
# str1 = 'a'
# print(str1 in str)
# print()

####################### list ######################
# lis = range(1,101)
# print(type(lis))
# print(list(range(0,100)))
# result = [a for a in lis if a %2 == 0]
# print(result)
# list = [1,2,3,4]
# list.append(5)
# result = list.insert(1,"a")
# result = list.extend([4,5,6])
# result = list * 3
# result = list + [5,6,7]
# print(list,result)
# list1 = [1,2,3,4,5,6,7,8,9]
# list2 = ["a","b","c"]
# list3 = ("-","=","*")
# str = "qwer"
# del list1[2]
# result = list1.pop(0)
# result = list1.remove(2)
# result = zip(list1,list2,list3,str)
# print(list(result))
# lis = ["a","b","c","d","e","f"]
# print(lis[-2])
# print(lis.index(1,5))
# print(lis.count(2))
# print(lis[4:0:-1])
# print(lis.find(1))
# lis = range(20,)
# for l in lis:
#     print(l,lis[l])
# index = range(len(lis))
# for i in range(len(lis)):
#     print(i,lis[i])
# for i,v in enumerate(lis):
#     print(i,v)
# import collections
# it = "asdf"
# i = iter(it)
# print(next(i))
# print(next(i))
# for x in i:
#     print(x)
# print(next(i))
# print(isinstance(i,collections.Iterator))
# print(("a") in ["a","b"])
# print([5,2] > [5,0])
# lis = [1,2,3,4,5,6,7]
# lis = list(enumerate(lis))
# def getKey(x):
#     return x[0]
# # print(sorted(lis,reverse = True))
# print(lis.sort(key = getKey,reverse = False))
# print(lis)
# import random
# random.shuffle(lis)
# print(lis)
# print(lis.reverse())
# print(lis)
# print(lis[::-1])
####################### tupule ###################
# tup = (1,)
# tup1 = 10,2,3
# # print(tup[0])
# print(type(tup))
# print(type(tup1))
# l = [1,2,3,4,5]
# print(tuple(l))
# t = (1,2,3,4,5,6,7,8,9)
# print(t.count(11))
# print(t[::-1])
# print(t.index(12))
# print(min(t))
# print(len(t))
# print(max(t))
# print(1 in t)
# print(1 not in t)
# print((2,3,4) > t)
# print(sorted(t,reverse = True))
# print(t*3)
# print(t+(12,2))
# print(t+(1,))
############# dict ######################
# dic = {1:"a",2:"b",3:"C",1:"d"}
# print(dic[1])
# print(type(dic))
# dic = dict.fromkeys("abcd", "abcd")
# str = {}.fromkeys("asdf","a")
# print(str)
# print(dic)
# dic = {}
# print(id(dic))
# dic["name"] = "Bruce Lee"
# dic["age"] = 18
# dic["height"] = 180
# dic["weight"] = 120
# del dic["age"]
# dic["sex"] = "男"
# del dic["sex"]
# print(dic,id(dic))
# print(dic)
# p = dic.pop("name1",66)
# print(p,dic)
# lis = ["a","b","c","d","e"]
# for i,x in enumerate(lis):
#     time.sleep(1)
#     print(x)
#     dic = dict.fromkeys(lis,x)

# time.sleep(5)
# print(dic)import time

# p1 = dic.popitem()
# print(dic)
# dic = {5:"e",4:"d",2:"C",1:"b",6:"a"}
# p = dic.popitem()
# print(p)
# print(dic)
# dic = {"name":"yang"}
# dic1 = {"age":18}
# dic.update(dic1)
# print(dic.update(dic1))
# print(dic,dic1)
# print(dic.get("name",666),dic)
# print(dic.setdefault("name",18),dic)
# print(dic.values())
# print(dic.keys())
# print(dic.items())
# print(list(enumerate(dic.items())))
# for v in zip(list(dic.keys()),list(dic.values())):
#     print(v)
# for x in zip(dic.keys(),dic.values()):
#     print(x[0],x[1])
# print(len(dic))
# dic = {"name":"Bruce Lee","age":32,"sex":"男"}
# print(dic.items())
# for k,v in dic.items():
#     print(k,v)
# print("name" in dic.keys())
################### set ####################
# str = "abc"
# print(id(str))
# str1 = "abcasdas"
# print(id(str))
# s = {2}
# s1 = set(["a","b","c"])
# print(s1)
# print(type(s),type(s1))
# s2 = {x for x in range(10) if x %2 == 0}
# print(s2)
# s3 = frozenset(x for x in range(20) if x %2 != 0)
# print(s3)
# s = {1,(2,3),"45"}
# print(s)
# str = "abc"
# str1 = "abc1"
# print(id(str),id(str1))
# print(id(str) == id(str1))
# lis = [1,2,3,4]
# lis1 = [1,2,3,4,5,2,23,5,3,2]
# s = list(set(lis1))
# print(s)
# s = {9,8,7,5,6}
# print(s)
# # result = s.remove(1)
# # result = s.discard(6)
# result = s.pop()
# print(result,s)
# result = s.pop()
# print(result,s)
# s.update([1,2,3])
# print(s)
# result = s.difference([1,9])
# print(s,result)
# s.isdisjoint()
# s1 = set([1,2,3])
# s2 = frozenset([3,4,5])
# print(s1.intersection(s2),s1&s2)
# print(s1.intersection_update([3,2,5]),s1)
# print({1,2,3} | {3,4,5})
# s1 = {1,2,3,4}
# s2 = frozenset([3,4,5,6])
# print(s1.remove(1),s1)
# print(s1.discard(6),s1)
# print(s1.intersection(s2),s1,sep = "|")
# print(s2.intersection(s1),s2,sep = "|")
# print(s1 & s2,s1)
# print(s2 & s1,s2)
# print(s1.intersection_update(s2),s1,sep = "|")
# print(s2.intersection_update(s1).s2,sep = "|")
# print(s1.union(s2),s1,s2,sep = "|")
# print(s2.union(s1))
# print(s1 | s2)
# print(s2 | s1)
# print(s1.update(s2))
# print(s1)
# s2.update(s1)
# print(s1.difference(s2))
# print(s2.difference(s1))
# print(s1-s2)
# s1.difference_update(s2)
# print(s1)
# s2.difference_update()
# s1 = {1,2,3,4,5,6}
# s2 = frozenset([1,2,3])
# print(s1.isdisjoint(s2))
# print(s1.issuperset(s2))
# print(s2.issubset(s1))

###################### 时间模块 ################
# import time
# t = time.time()
# year = t / (24 * 60 * 60 * 365) + 1970
# print(year)
# result = time.localtime()
# print(result)
# t = time.time()
# t = time.time()
# print(time.ctime(t))
# time_tuple = time.localtime()
# print(time.asctime(time_tuple))
# time_tuple = time.localtime()
# result = time.strftime("%Y-%m",time_tuple)
# print(result)
# import calendar
# print(calendar.January(2018,12))
# print(calendar.month)
# import datetime
# print(datetime.datetime.now())
# print(datetime.datetime.ctime())
# t = datetime.datetime.now()
# print(t.year)
# print(t.month)
# print(t.date)
# print(t.weekday)
# print(t.day)
# print(t.minute)
############# function ###############
# def test(x):
    # print(x**3)
# test(26)
# def test(num1,num2):
#     print(num1 + num2,num1,num2)
# test(1, 2)
# test(num2 = 2,num1 = 3)
# def info(name,age):
#     print(name,age)
# def test(**kwargs):
#     print(kwargs)
#     info(**kwargs)
# test(age = 18,name = "bruce")
# def test(name = "Bruce"):
    # print("我的名字是{}".format(name))
# test("yang")
# def test(num):
#     print(id(num))
#     num.append(6)
#     print(id(num),num)
# aa = [1,2,3]
# print(id(aa),aa)
# test(aa)
# print(id(aa),aa)
# def test():
#     cha = 10-9
#     he = 10+9
#     return (cha,he)
# a,b = test()
# print(a)
# def test(a,b):
#     """
#     你好
#     """
#     pass
# help(test)
# def test(a,b,c,d):
#     return a+b+c+d
# def test1(a,b,c,d=10):
#     return test(a,b,c,d)
# import functools
# newfunc = functools.partial(test1,c=5)
# result = newfunc(1,2)
# print(result)
# str = "10010"
# import functools
# new_int = functools.partial(int,base = 2)
# num = new_int(str)
# print(num)
# functools.partial()
# def jia(x,y):
#     print(x + y)
# def caculater(*args,**kwargs):
#     kwargs["func"](*args)
# caculater(10,30,func = jia)
# def test1():
    # def test2():
        # print(123)
    # return test2
# result = test1()()
# dic  = {"d":1,"c":2,"b":1,"a":0}
# print(sorted(dic, key =, reverse = False))
# print(dic)
# result = (lambda x,y : x ** y)(5, 5)
# print(result(3,4))
# print(result)
# sorted(iterable, key, reverse)
# help(sorted)
# def test(content,filler,length):
#     def inner():
#         print("{0}{1}{0}".format(filler*length,content))
#     return inner
# result = test("xxxxx","-",10)
# result()
# result()
# result = test("aaaaa","+",10)
# result()
# result()
# def test():
#     num = 10
#     def test1():
#         nonlocal num
#         num = 66
#         print(num,"local")
#     test1()
#     print(num,"globle")
#     return test1
# result = test()
# result()
# def test():
#     funcs = []
#     for i in range(1,4):
#         def test1(i):
#             num = i
#             def inner():
#                 print(num)
#             return inner
#         funcs.append(test1(i))
#     return funcs
# result = test()
# result[0]()
# result[1]()
# result[2]()
# def jc(func):
#     def inner():
#         print("验证")
#         func()
#     return inner
# @jc
# def fss():
#     print("发说说")
# def ftp():
#     print("发图片")

# num = 2
# if num == 2:
#     fss()
# else:
#     ftp()
# y = (i for i in range(10))
# print(y.__next__())
# print(type(y))
# a = 10 
# def test():
#     print(a)
#     def inner():
#         print(a)
#     return inner
# test()()
# pic = open("aa.jpeg","rb")
# pic_r = pic.read()
# f = open("bb.jpeg","wb")
# pic_r = pic_r[0:(len(pic_r)//2)]
# f.write(pic_r)
# f.close()
# pic.close()
# with open("test.text","r",encoding = "utf8") as f:
#     f.seek(2)
#     t = f.tell()
#     print(t)
# import os
# f = open("test/test.txt","w")
# f.write("123456")
# f.close()
# print(os.listdir("test/"))
# os.rename("test1.txt","test/test1.txt")
# os.renames("test/aa.txt","test/t1/dd.txt")
# os.remove("test/t1/d2/d3/d.txt")
# os.rmdir("test/t1/d2/d3/")
# result = os.removedirs("d1/d2/d3/")
# print(result)
# os.mkdir("d1/d2/d3/d4")
# os.rmdir("d1/d2/d3/")
# os.removedirs("d1/d2/d3/d4/"
# os.mkdir("d1/d2/d3/d4",mode = 0o444)
# f = open("d1/d2/d3/d4/aa.txt","w")
# f.write("abc")
# f.close()
# print(os.getcwd())
# print(os.chdir("d1/d2/d3/"))
# print(os.getcwd())
# os.remove("aa.txt")
# print(os.listdir("d1"))
# import os
# os.chdir("d1/d2/")
# os.remove("d.txt")
# os.chdir("d1/")
# os.removedirs("d2/d3/d4")
# os.makedirs("d1/d2/d3")
# os.rmdir("d1/d2/d3/")
# os.mkdir("d1/d3")
# with open("d1/d2/t1.txt","w") as f:
#     f.write("123")
# with open("d1/d2/t1.txt","r",encoding = "utf-8") as t1,open("d1/d3/t2.txt","a",encoding = "utf-8") as t2:
#     while True:
#         content = t1.read(100)
#         if len(content) == 0:
#             break
#         t2.write(content)
# print(os.path.isfile("d1/d2/t1.txt"))
# print(os.path.isabs("d1/d2/t1.txt"))
# help(os.path.islink)
# print(os.path.islink("www.baidu.com/d1/"))
# print(os.path.split(os.getcwd()))
# print(os.path.join())
# print(os.path.abspath("d1/"))
# print(os.path.basename("d1/d2/t1.txt"))
# print(os.path.commonprefix(["abcd2","abcd1"]))
# print(os.path.islink())
# print(os.path.dirname("d1/d3/t2.txt"))
# print(os.path.exists("d1/d3/"))
# print()
# help(os.isatty)
# import os,time
# print(time.ctime(os.path.getmtime("d1/")))
# print( time.gmtime(os.path.getmtime("d1/")) )
# import os,random
# import shutil
# # 生成十个随机文件
# os.chdir("d1/")
# lisdir = os.listdir()
# if len(lisdir) < 0:
#     lis = "".join([chr(x) for x in range(97,122)])
#     extension = ["txt","avi","jpeg","png","zip"]
#     for x in range(10):
#         rd_name = "".join(random.sample(lis,4))
#         rd_extension = random.choice(extension)
#         file_name = "{0}.{1}".format(rd_name,rd_extension)
#         f = open(file_name,"w")
#     f.close() 
# for ld in lisdir:
#     if not os.path.isfile(ld):
#         continue
#     index = ld.rfind(".")
#     hz = ld[index+1:len(ld)]
#     print(hz)
#     # 判断此后缀后缀名是否存在文件夹
#     if not(os.path.isdir(hz)):
#         os.mkdir(hz)
#     shutil.move(ld,hz)
# import os
# def listFiles(dir):
#     file_list = os.listdir(dir)
#     for file_name in file_list:
#         new_fileName = os.path.join(dir,file_name)
#         if os.path.isdir(new_fileName):
#             print(new_fileName)
#             listFiles(new_fileName)
#         elif os.path.isfile(new_fileName):
#             print("--"+os.path.basename(new_fileName))
# os.mknod("list.txt")
# listFiles("d1")
# print(os.sep)
# print(os.name)
# result = os.sep.join("{0}{1}".format("abc","ess"))
# print(result)
# p = Persen
# print(Persen.__name__)
# print(p.__name__)
# print(persen.__class__ == Persen)
# class Persen:
#     pass
# persen = Persen()
# persen.name = "Bruce Lee"
# persen.age = 32
# persen.friends = ["yang","zhu"]
# print(persen.friends,id(persen.friends))
# persen.friends.append(["hong"])
# print(persen.friends,id(persen.friends))
# print(Persen.__dict__)
# print(persen.__dict__)
# del persen.name
# print(persen.__dict__)
# print(persen.age)
# class Persen:
#     name = "Bruce Lee"
#     age = 18
# Persen.address = "上海"
# one = Persen()
# # one.name = "zhang"
# class Test:
#     na.name)me = "yang"
# one.__class__ = Test
# print(one
# print(Persen.address)\]
# class Persen:
#     name = "Bruce Lee"
# one = Persen()
# print(Persen.name,id(Persen.name))
# print(one.name,id(one.name))
# one.name = "wanglihong"
# print(Persen.name,id(Persen.name))
# print(one.name,id(one.name))
# del one.name
# del one.name
# del Persen.name
# print(one.name)
# class Persen:
#     name = "Bruce Lee"
# one = Persen()
# Persen.name = "yang"
# print(Persen.name)
# # Persen.__dict__["name"] = "li"
# print(one.name)
# one.__dict__["name"] = "yang"
# print(one.__dict__)
# print(one.name)
# class Persen:
    # age = 18
# one = Persen()
# two = Persen()
# print(one.age)
# print(two.age)
# Persen.age = 20
# print(one.age,two.age)
# class Persen:
#     age = 10
# one = Persen()
# one.age += 5
# print(Persen.age)
# print(one.age)
# class Persen:
#     __slots__ = ["age"]
# p1 = Persen()
# p2 = Persen()
# p1.age = 18
# p2.age = 15
# print(p1.age,p2.age)
# p2.name = 'zhang'
# class Persen:
#     def obj(self):
#         print("实例方法",self)
#     @classmethod
#     def cls(cls):
#         print("类方法",cls)
#     @staticmethod
#     def sta():
#         print("静态方法")
# p1 = Persen()
# persen = Persen
# p1.sta()
# persen.sta()
# p1.obj()
# print(p1)
# # persen.obj()
# p1.cls()
# print(p1.__class__)
# persen.cls()
# print(persen)
# class Persen:
#    @classmethod
#    def aa(cls):
#         print(cls)
# Persen.aa()
# class Son(Persen):
#     pass
# Son.aa()
# def run(self):
#     print(self)
# @classmethod
# def eat(cls):
#     print(cls)
# @staticmethod
# def play():
#     print("静态")
# Persen = type("Persen",(),{"age":18,"run":run,"eat":eat,"play":play})
# print(Persen.__name__)
# print(Persen.__dict__)
# p = Persen()
# p.eat()
# p.play()
# p.run()
# class SayMataClass(type):
#     def __new__(cls,name,bases,attrs):
#         attrs["say_" + name] = lambda self,value,saying = name : print("|" + saying + "," + value + "|")
#         return type.__new__(cls,name,bases,attrs)
# class Hellow(metaclass=SayMataClass):
#     pass
# class Hi(metaclass = SayMataClass):
#     pass
# hellow = Hellow()
# hellow.say_Hellow("word")
# hi = Hi()
# hi.say_Hi("word")
# from getpage import get_page
# from pyquery import PyQuery as pq


# # 道生一：创建抽取代理的metaclass
# class ProxyMetaclass(type):
#     """
#         元类，在FreeProxyGetter类中加入
#         __CrawlFunc__和__CrawlFuncCount__
#         两个参数，分别表示爬虫函数，和爬虫函数的数量。
#     """
#     def __new__(cls, name, bases, attrs):
#         count = 0
#         attrs['__CrawlFunc__'] = []
#         attrs['__CrawlName__'] = []
#         for k, v in attrs.items():
#             if 'crawl_' in k:
#                 attrs['__CrawlName__'].append(k)
#                 attrs['__CrawlFunc__'].append(v)
#                 count += 1
#         for k in attrs['__CrawlName__']:
#             attrs.pop(k)
#         attrs['__CrawlFuncCount__'] = count
#         return type.__new__(cls, name, bases, attrs)


# # 一生二：创建代理获取类

# class ProxyGetter(object, metaclass=ProxyMetaclass):
#     def get_raw_proxies(self, site):
#         proxies = []
#         print('Site', site)
#         for func in self.__CrawlFunc__:
#             if func.__name__==site:
#                 this_page_proxies = func(self)
#                 for proxy in this_page_proxies:
#                     print('Getting', proxy, 'from', site)
#                     proxies.append(proxy)
#         return proxies


#     def crawl_daili66(self, page_count=4):
#         start_url = 'http://www.66ip.cn/{}.html'
#         urls = [start_url.format(page) for page in range(1, page_count + 1)]
#         for url in urls:
#             print('Crawling', url)
#             html = get_page(url)
#             if html:
#                 doc = pq(html)
#                 trs = doc('.containerbox table tr:gt(0)').items()
#                 for tr in trs:
#                     ip = tr.find('td:nth-child(1)').text()
#                     port = tr.find('td:nth-child(2)').text()
#                     yield ':'.join([ip, port])

#     def crawl_proxy360(self):
#         start_url = 'http://www.proxy360.cn/Region/China'
#         print('Crawling', start_url)
#         html = get_page(start_url)
#         if html:
#             doc = pq(html)
#             lines = doc('div[name="list_proxy_ip"]').items()
#             for line in lines:
#                 ip = line.find('.tbBottomLine:nth-child(1)').text()
#                 port = line.find('.tbBottomLine:nth-child(2)').text()
#                 yield ':'.join([ip, port])

#     def crawl_goubanjia(self):
#         start_url = 'http://www.goubanjia.com/free/gngn/index.shtml'
#         html = get_page(start_url)
#         if html:
#             doc = pq(html)
#             tds = doc('td.ip').items()
#             for td in tds:
#                 td.find('p').remove()
#                 yield td.text().replace(' ', '')


# if __name__ == '__main__':
#     # 二生三：实例化ProxyGetter
#     crawler = ProxyGetter()
#     print(crawler.__CrawlName__)
#     # 三生万物
#     for site_label in range(crawler.__CrawlFuncCount__):
#         site = crawler.__CrawlName__[site_label]
#         myProxies = crawler.get_raw_proxies(site)
# class Person:
#     def __init__(self):
#         self.__age = 18

#     @property
#     def age(self):
#         return self.__age
# p = Person()
# print(p.age)
# p.age = 20
# print(p.age)
# print(p.age)
# p.age = 20
# print(p.age())
# class Person(object):
#     def __init__(self):
#         self.__age = 18
#     def fget_age(self):
#         return self.__age
#     def fset_age(self,value):
#         self.__age = value
#     def fdel_age(self):
#         del self.__age
#     age = property(fget_age,fset_age,fdel_age)
# # print(Person.__dict__)
# class Person:
#     def __init__(self):
#         self.__age = 18
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self,value):
#         self.__age = value
#     @age.deleter
#     def age(self):
#         del self.__age
# p = Person()
# print(p.age)
# p.age = 20
# print(p.__dict__)
# print(p.age)
# del p.age
# print(p.__dict__)
# print(p.age)
# help(property)
# class Person:
#     "nihoa"
#     def __init__(self):
#         self.__age = 18
#     def __getattr__(self,attr):
#         if attr not in self.__dict__.keys():
#             return "不存在！"
#     def __setattr__(self,attr,value):
#         if attr == "age" and attr in self.__dict__.keys():
#             print("只读属性")
#         else:
#             self.__dict__[attr] = value
#     @property
#     def age(self):
#         return self.__age  
    
# p = Person()
# print(Person.__class__)
# print(Person.__dict__)
# print(Person.__doc__)
# print(Person.__base__)
# print(Person.__bases__)
# print(Person.__name__)
# print(Person.__module__)
# print(p.__class__)
# print(p.__dict__)
# print(p.__name__)
# print()
# print(Person.)
# print(p.age)
# # print(p._Person__age)
# print(p.__dict__)
# p.name = 18
# print(p.age)

# class Context:
#     def __enter__(self):
#         return 123
#     def __exit__(self,a,b,c):
#         print(a,b,c,sep = "\n")
#         import traceback
#         print(traceback.extract_stack())
#         # print(traceback.extract_tb(c))
#         # print(traceback.format_exception_only(a,b))
#         # print(traceback.format_list(b))
#         return True
# with Context() as f:
#     print(f)
#     print(1/0)
# import contextlib
# @contextlib.contextmanager
# def test():
#     try:
#         f = open("test.text","r")
#         yield f
#     except Exception as e:
#         print(e)
#     finally:
#         print("C")
# with test() as a:
#     print(a.read())
#     print(1/0)
# class Person:
#     def __str__(self):
#         return "str"
#     def __repr__(self):
#         # print("repr")
#         return "repr"
# p = Person()
# print(p)
# print(repr(p))
# p = input("123")
# print(repr(p),type(repr(p)))
# print(eval(repr(p)),type(eval(repr(p))))
# class Person:
#     def __init__(self,type):
#         self.type = type
#     def __call__(self,color):
#         print("您创建了一个{},颜色是{}".format(self.type,color))
# p = Person("钢笔")
# p("红色")
# p("青色")
# p1 = Person("铅笔")
# p1("红色")
# p1("绿色")
# class Person:

#     def __init__(self):
#         self.__cache = {}
#         self.__lis = [1,2,3,4,5,6,7]

#     def __getitem__(self,k):
#         # print(k.start)
#         # print(k.stop)
#         # print(k.step)
#         # return self.lis[k.start:k.stop:k.step]
#         if isinstance(k,slice):
#             return self.__lis[k]

#     def __setitem__(self,k,v):
#         # print(k,v)
#         # self.lis[k.start:k.stop:k.step] = v
#         if isinstance(k,slice):
#             self.__lis[k] = v

#     def __delitem__(self,k):
#         if isinstance(k,slice):
#             del self.__lis[k]

#     def __str__(self):
#         return str(self.__lis)
# p = Person()
# print(p[0:3])
# p[0:3] = ["a","b"]
# print(p)
# print(p[0:3])
# del p[0:3]
# print(p)
# class Vs:

#     def __init__(self,age,height):
#         self.age = age
#         self.height = height
#     def __eq__(self,other):
#         print(self.__dict__,other.__dict__,"eq")
#         return self.age == other.age

    # def __ne__(self,other):
    #     print(self.__dict__,other.__dict__,"ne")
    # #     return self.age != other.age

    # def __gt__(self,other):
    #     print(self.__dict__,other.__dict__,"gt")
    #     return self.age > other.age

    # def __ge__(self,other):
    #     print(self.__dict__,other.__dict__,"ge")
    #     return self.age >= other.age

    # def __lt__(self,other):
    #     print(self.__dict__,other.__dict__,"lt")
    #     return self.age < other.age

    # def __le__(self,other):
    #     print(self.__dict__,other.__dict__,"le")
    #     return self.age <= other.age

# v1 = Vs(18,180)
# v2 = Vs(17,180)
# print(v1==v2)
# print(v1!=v2)
# print(v1 > v2)
# print(v1 >= v2)
# print(v1 < v2)
# print(v1 <= v2)
# class Person:
#     def __init__(self,age):
#         self.age = age
#     def __bool__(self):
#         return self.age > 18
# p = Person(18)
# if p:
#     print("成年了")
# else:
#     print("未成年")
# class Person:
#     def __init__(self):
#         self.lis = [1,2,3,4,5]
#         self.index = -1
#     def __iter__(self):
#         self.index = -1
#         return self
#     def __next__(self):
#         self.index += 1
#         if self.index < len(self.lis):
#             return self.lis[self.index]
#         else:
#             raise StopIteration("超出范围")
# p = Person()
# import time
# for x in p:
#     # time.sleep(1)
#     print(x)
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# for x in p:
#     print(x,"-")

# for x in p:
#     print(x,"-")
# class Person:

#     def __init__(self):
#         self.list = [1,2,3,4,5,6,7]
#         self.index = -1

#     # def __getitem__(self,item):
#     #     self.index += 1
#     #     if self.index < len(self.list):
#     #         return self.list[self.index]
#     #     else:
#     #         raise StopIteration("超出停止")
#     def __iter__(self):
#         return self 

#     def __next__(self):

#         self.index += 1
#         if self.index < len(self.list):
#             return self.list[self.index]
#         else:
#             raise StopIteration("超出停止")
#     def __call__(self):

#         self.index += 1
#         if self.index < len(self.list):
#             return self.list[self.index]
#         else:
#             raise StopIteration("超出停止")

# import collections
# p = Person()
# p = iter(p,6)
# print(next(p))
# for x in p:
#     print(x,"-")
# class Descriptor:

#     def __get__(self,instance,owner):
#         print("Get")
#         # print(instance)
#         # print(self,instance,owner)
#         # instance.age = 11
#         return instance

#     def __set__(self,isinstance,value):
#         print("set")

#     def __delete__(self):
#         print("del")

# class Person:
#     # weight = Descriptor()
#     age = Descriptor()
#     def __init__(self):
#         # self.age = 10
#         pass

#     def __getattr__(self,k):
#         print("getattr")
#         self.age = 20
#         return self.age
# # .
# #     def __setattr__(self,k,v):
# #         print("setattr",k,v)

# #     def __delattr__(self):
# #         print("delattr")

#     # def __getattribute__(self,k):
#     #     print("getattribute",k)
#     #     self.age = 21
#     #     return self.age



# p = Person()
# # print(p.__dict__)
# print(p.age)
# print(Person.age)
# print(p.age == p)
# print(p.age)
# print(p._Person__age)
# # print(p.__dict__)
# # p.age = 19
# # print(p.__dict__)
# # print(Person.age)
# print(Person.__dict__)
# print(p.__self__)
# class obj:

#     def __init__(self):
#         self.list = [1,2,3,4,5,6,7]
#         self.index = -1

#     # def __getitem__(self,item):
#     #     self.index += 1
#     #     if self.index < len(self.list):
#     #         return self.list[self.index]
#     #     else:
#     #         raise StopIteration("终止")

#     def __iter__(self):
#        return self

#     def __next__(self):
#         self.index += 1
#         if self.index < len(self.list):
#             return self.list[self.index]
#         else:
#             raise StopIteration("终止")

# import collections
# o = obj()
# print(isinstance(o,collections.Iterable))
# print(isinstance(o,collections.Iterator))
# o = iter(o)
# print(next(o))
# for x in o:
#     print(x,"-")
# class Descriptor:

#     def __get__(self,instance,owner):
#         print("get",self,instance,owner)

#     def __set__(self,instance,value):
#         print("set",self,instance,value)

#     def __delete__(self,instance):
#         print("delete",self,instance)

# class Person:

#     # age = Descriptor()
#     # age = 18 
#     def __init__(self,age):
#         self.age = age

#     def __getattr__(self,k):
#         print("getattr",k)

#     def __setattr__(self,k,v):
#         print("setattr",k,v)
#         # self.__dict__[k] = v
#         super().__setattr__(k, v)

#     def __delattr__(self,k):
#         print("deattr")


# p = Person(18)
# print(p.age)
# print(p.__dict__)
# print(Person.__dict__)
# p.age = 18
# del p.age



# p = Person()
# print(isinstance(p,Person))
# print(person.age)
# class RevealAccess(object):
#     def __init__(self, initval=None, name='var'):
#         self.val = initval
#         self.name = name
#         print(self,self.name,"-")
#     def __get__(self, obj, objtype):
#         print('Retrieving',self,obj,objtype)
#         return self.val
#     def __set__(self, obj, val):
#         print('Updating', self.name)
#         self.val = val

# class MyClass(object):
#     x = RevealAccess(10, 'var "x"')
#     y = 5
# class Animal:
#     def __init__(self,attr = None, value = None):
#         self.attr = value

#     def __get__(self,instance,woner):
#         return instance.attr

#     def __set__(self,instance,value):
#         instance.attr = value 

#     def __delete(self,instance):
#         del instance.attr

# class Person:

#     __age = Animal("age",18)

#     def __getattr__(self,attr):
#         return "{}不存在".format(attr)

# p = Person()
# p.age = 19
# print(p.age)
# def cl(fun):
#     def inner(**kyword):
#         print("-"*6,"验证")
#         # args(**kyword)
#         fun(**kyword)
#     return inner
# class cl:
#     def __init__(self,fun):
#         self.fun = fun
#     def __call__(self,*args,**kyword):
#         print("-"*6)
#         self.fun(**kyword)
# @cl
# #fss = cl(fss) 
# def fss(**kyword):
#     print("{name}在发说说".format(**kyword))
# fss(name = "yang")
# class SayMataClass(type):
#     def __new__(cls,name,bases,attrs):
#         # print(cls,name,bases,attrs,sep = "-")
#         attrs["say_" + name] = lambda self,value,saying = name : print("|" + saying + "," + value + "|")
#         return type.__new__(cls,name,bases,attrs)

# class Person(metaclass=SayMataClass):
#     # def __new__(*args):
#     #     print(*args)
#     #     # return type.__new__(**kyword)
#     # def (self):
#         # pass
#     def __init__(self):
#         print(self)

# p = Person()
# p.say_Person("word")
# class Animal:

#     def __init__(self):
#         print("Animal")
#         # self.age = 18

# class Person(Animal):

#     def __new__(cls,*args,**kwargs):
#         print(args,kwargs,sep = "-")
#         return super().__new__(Animal, *args, **kwargs)

#     def __init__(self):
#         self.age = 20
#         print("persen")

# p = Person()
# a = Animal()
# print(a.age)
# print(p.age)
# class Person:
#     __count = 0
#     def __init__(self):
#         Person.__count += 1

#     def __del__(self):
#         Person.__count -=1
#     @classmethod
#     def log(cls):
#         print("计数为{}".format(cls.__count))

# p = Person()
# Person.log()

# p2 = Person()
# Person.log()
# import sys
# print(sys.getrefcount(p))
# del p
# print(sys.getrefcount(Person))
#
# import gc
# print(gc.get_threshold())
# gc.set_threshold(100,5,5)
# print(gc.get_threshold())
# gc.disable()
# gc.enable()
# print(gc.isenabled())
# import win32com.client
# speaker = win32com.client.Dispatch("SAPI.SpVoice")
# class Js:

#     def check(fun):
#         def inner(self,num):
#             if not isinstance(num,int):
#                  speaker.Speak("{}不是一个数字，不能参与运算".format(num))
#                  exit()
#                 # raise TypeError("{}不是一个整形".format(num))




#             return fun(self,num)
#         return inner

#     def __say(word = ""):
#         def say(fun):
#             def inner(self,n = ""):
#                 speaker.Speak("{}{}".format(word,n))
#                 return fun(self,n)
#             return inner 
#         return say

#     @check
#     @__say()
#     def __init__(self,shu):
#         self.__shu = shu

#     @check
#     @__say("+")
#     def jia(self,jiashu):
#         self.__shu += jiashu
#         return self

#     @check
#     @__say("减去")
#     def jian(self,jianshu):
#         self.__shu -+ jianshu
#         return self

#     @check
#     @__say("乘以")
#     def cheng(self,chengshu):
#         self.__shu *= chengshu
#         return self

#     @check
#     @__say("除以")
#     def chu(self,chushu):
#         self.__shu /= chushu
#         return self

#     @property
#     def dengyu(self):
#         speaker.Speak("={}".format(self.__shu))
#         print(self.__shu)

# Js(2).cheng(5).jia(6).cheng(50).chu(3).dengyu
# def check(fun):
#     def inner():
#         print("验证操作")
#         return fun()
#     return inner
# @check
# def fss():
#     print("发说说")

# fss()
# class D:
#     name = "D"

# class B(D):
#     # name = "B"
#     pass

# class C(D):
#     # name = "C"
#     pass

# class A(B,C):
#     # name = "A"
#     pass

# a = A()
# print(a.name)
# class D:
#     # name = "D"

# class C(D):
#     # name = "C"
#     pass

# class B(C):
#     # name = "B"
#     pass

# class A(B):
#     # name = "A"
#     pass

# a = A()
# print(a.name)
# class E:
#     name = "E"
#     pass

# class D(E):
#     name = "D"
#     pass

# class B(D):
#     name = "B"
#     pass

# class C(B):
#     name = "C"
#     pass

# class A(B,C):
#     name = "A"
#     pass

# a = A()

# # print(a.name)
# print(A.__mro__)
# arr = [[1,2,3,4,5,6],[2,3,[2,3,4],4,5,6,7],[3,4,5,[3,4,5,6,10],6,7,8],[4,5,6,7,8,9]]
# lis = []
# def get_num(num,arr):
#     for x in arr:
#         if isinstance(x,list):
#             get_num(num,x)
#         else:
#             lis.append(x)
#     return num in set(lis)

# if __name__ == "__main__":
#     result = get_num(1,arr)
#     print(result)
#     
# class MetaAnimal(type):
#     def __new__(cls,name,bases,attrs):
#         attrs["play"] = lambda name: print("{}在玩".format(name))
#         attrs["sleep"] = lambda name: print("{}在睡觉".format(name))
#         attrs["eat"] = lambda name: print("{}在吃饭".format(name))
#         attrs["names"] = name
#         return super(MetaAnimal,cls).__new__(cls,name,bases,attrs)

# class Animal(metaclass = MetaAnimal):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
   
#     def work(self,obligation):
#         print("{}在{}".format(self,obligation))

#     def __str__(self):
#         return "名字是{},年龄是{}岁的{}".format(self.name,self.age,self.names)
        
# class Dog(Animal):
#     def work(self):
#         super().work("看家")

# class Cat(Animal):
#     def work(self):
#         super().work("捉老鼠")

# class Person(Animal):
#     def __init__(self,name,pats,age = 1):
#         super().__init__(name,age)
#         self.pats = pats

#     def rangwork(self):
#         for pat in self.pats:
#             pat.work()

#     def yangchongwu(self):
#         print("{}养{}个宠物,一个{}和另一个{}".format(self,len(self.pats),self.pats[0],self.pats[1]))

# d = Dog("小黑",18)
# d.play()
# c = Cat("小红",3)
# c.sleep()
# c.work()
# p = Person("小张",[d,c],20)
# p.yangchongwu()
# print("-"*30)
# p.rangwork()
# str = "bcbaefg"
# print(str[::-1])
# result = str.find("a",0,3)
# print(result)
# result = str.count(sub, start, end)
# print()
# from functools import reduce
# reduce(lambda x,y:print(x+y),[1,2,3,4,5])
# lis = [1,2,3]
# lis.insert(0,[4,5])
# print(lis)
# lis.extend([1,2,3])
# print(lis)
# lis = [1,2,3,2]
# # lis.remove(2)
# lis = [x for x in lis if x != 2]
# print(lis)
# lis = enumerate([1,2,3,4,5,6])
# for k,v in lis:
#     print(k,v)
# issubclass(, class_or_tuple)
# str = "abcdefg"
# def test():
#     lis = []
#     for x in str:
#         def inner():
#             lis.append(x)
#             return lis
#         return inner
# # print(dic)
# print(test()())
# print(test()())
# aa = (x for x in range(20))
# print(value)
# import re
# str = "aabab"
# result = 
# dic = {"name":"yang"}
# print(dic['name'])
# import threading
# import time
# def song():
#     for x in range(5):
#         print("--------唱歌-----------\n")
#         time.sleep(1)
#         print("song over")

# def dance():
#     for x in range(5):
#         print("---------跳舞-----------\n")
#         time.sleep(1.2)
#         print("dance over")

# t1 = threading.Thread(target=song)
# t2 = threading.Thread(target=dance)
# tread = [t1,t2]

# for t in tread:
#     t.start()
# t1.join()

# print(threading.enumerate())
# print("all over")