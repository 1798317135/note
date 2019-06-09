# *************************** re模块可以让python 使用全部的正则语法
import re
# #*************** re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
# str = "aaBab"
# exp = re.match(r'(a)(.*?b)', str,re.I | re.M)
# print(exp.group())
# print(exp.groups())
# if exp:
#     for x in exp.group():
#         print(x)
# else:
#     print("no exp")

# *************** re.search 扫描整个字符串并返回第一个成功的匹配。
# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，
# 则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。

# str = "asdfyangasdhellow,asdfkjyang"
# exp = re.search(r'^\w+(?P<name>yang)\w(.+)$',str,re.I | re.M)
# print(exp.groups())
# if exp:
#     print(exp.group())
# else:
#     print("no exp")

# ***************   re.sub用于替换字符串中的匹配项
        # re.sub(pattern, repl, string, count, flags)
        # pattern : 正则中的模式字符串。
        # repl : 替换的字符串，也可为一个函数。
        # string : 要被查找替换的原始字符串。
        # count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
        # 
# 也可以直接对替换的原始字符串 在函数里面处理 然后调用这个函数体
# 这里我们用到(?P<one>) 他的意思是给这个匹配的组命名
# 然后可以在group('one') 里面提取指定命名的组
# 
# def double(exp):
#     val = int(exp.group('one'))
#     return str(val + 2)
# s = 'asdf5sdf5sdf4sdf'
# exp = re.sub(r'(?P<one>\d+)',double,s)
# if exp:
#     print(exp)
# else:
#     print(4546)
# # print(str)

#
# ***************  (?P<name>) 这个组起一个名称,这个名称在这一个正则当中只能出现一次
# 
# *************** (?P=name) 在查询里面可以在此调用 name 组的匹配的值
#                 在替换中 而是(\g<name>)
#      
# s = 'asdfyangsdfadyangfszhenasdfyu'
# exp = re.sub(r'YANG',"---",s,0,re.I)
# print(exp,s)
#

# *************** compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象
#               ，供 match() 和 search() 这两个函数使用。
#   
# re.compile(pattern, flags)
# pattern : 一个字符串形式的正则表达式
# flags : 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
# re.I 忽略大小写
# re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
# re.M 多行模式
# re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
# re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
# re.X 为了增加可读性，忽略空格和 #后面的注释
# s = 'adsf123sdf454sdf5'
# pattern = re.compile(r'.{5}',re.I|re.M)
# m = pattern.match(s)
# print(m.group())
# print(m.start())
# print(m.end())
# print(m.span())
# 在上面，当匹配成功时返回一个 Match 对象，其中：
# group([group1, …]) 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)；
# start([group]) 方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；
# end([group]) 方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；
# span([group]) 方法返回 (start(group), end(group))。

# **********findall
# 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。

# 注意： match 和 search 是匹配一次 findall 匹配所有。
# s = 'asdfyangasdfzhensdfasyanglsdyu'
# pattern = re.compile(r'.*(yang).*?(zhen).*?(yu)',re.I|re.M)
# result = pattern.match(s)
# print(result.groups())

# **********re.finditer
# 和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。

# it = re.finditer(r'\d+','asdf5sdf5sadf56ad')
# for x in it:
#     print(x.group())

# # (?=) 正向肯定预查  aa(?bb|cc|dd) 可以是其中的一项
# # (?!) 正向否定预查 aa(?!bb|cc|dd) 不可以是其中的一项
# # (?<=) 反向肯定鱼叉 (?<=aa|bb|cc)ee
# # (?<!) 反向否定预查 (?<!aa|bb|cc)ee
# print_time()
#re.split
# split 方法按照能够匹配的子串将字符串分割后返回列表：
# s = 'aasdfsdfaasyangdfasyangfaasdfasdfaa'
# pattern = re.compile(r'yang',re.I|re.M)
# result = pattern.split(s,2)
# print(result.start())
# print(result.end())
# print(result)

