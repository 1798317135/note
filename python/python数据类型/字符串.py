
print("#\n\n **************************** 字符串的换行和嵌套  *****************************\n\n")
# 
# 
# 1.0  #################### 字符串的声明 规范 #####################
#
str1 = "aaaa"

str2 = 'aaaa'

str3 ='''aaaa'''

str4 = """aaaa"""

print(type(str1),type(str2),type(str3),type(str4))

# end ################## 字符串的声明 规范  ###########################
# 
# 
# 2.0 ################## 字符串的换行拼接 和 原字符串 ##################
# 
# --- 2.1 \ 是转义符放到最后就是续航符号 \t制表符 \n换行符
str = "我是东风科技"\
"十六大开发建立科技"
print(str)

# --- 2.2 用()括起来也可以练成一个整体 不用使用续航符号\
str = ("萨拉肯德基疯"
    "狂拉升封"
    "sdfasdf"
    )
print(str)
# --- 2.3 开头r代表原始字符串 不会对字符串里面的任何内容进行修改

str = r"你好呵呵\n撒旦法\t"
print(str)

# --- 2.4 """aaa""" 或者 '''aaa''' 都可以换行或者注释 里面也也可以使用单引号或者双引号对
str = '''你撒地方
'老卡'机"立刻"地方
sdfasdf
456456
'''
print(str)
# end ################## 字符串的换行拼接 和 原字符串 ####################
# 

# 3.0 ########################## 字符串拼接  ############################
# 
# 
# --- 3.1 字符串的连接 + 号 和 ,号
# 
str = "会撒谎的发挥的",11,"asdfadsf"
print(str,"|,")

# --- 3.2 占位符
# 
str = "撒地方建立科技%s%d" % ("asdfasdf",1+3)

print(str,"占位符")

str = "aa{0}bb{1}dd{2}".format("站位一","站位二","展位三")

print(str,"|.format()")

# #############################  字符串乘法 ##############################
# 
# --- 字符串的乘法 * 几次打印几次
# 
str = "是打发打发"

print(str*4)

# #############################  字符串切片 ##############################
# 
# 
str = "你好呵呵爱的色放"
print(str[2])
print(str)

# --- str[-1]从尾部开始数
print(str[-1],str[-2],"str[-1]从尾部开始数")

# --- 获得多个索引的区间[起始:结束:步长] 不包括结束位置

print(str[0:3:1])

# --- 默认
print(str[0:len(str):1],"默认")

# --- 如果步长为正数 是从左到右边 如果步长为负数是从右到左的，并且起始位置大于结束位置
# 
print(str[-1:-3:-1],"如果步长为正数 是从左到右边 如果步长为负数是从右到左的，并且起始位置大于结束位置")

# --- 翻转字符串 如果起始和结束都为默认 step设为-1 就从右到左依此反转

print(str[::-1],"翻转字符step -1")

# ############################  字符串的 内置函数 和 对象方法 #######################
# 
# ************************ 查找计算类 **********************
# 
print(str)
# --- len() 是一个python内置函数 用于计算字符长度 从1开始
str = "abcdeabfg"
print(len(str),"len()")

# --- find(sub,strat = 0 ,end = len(str)) 超找指定字符串的位置索引 如果没有找到则返回-1
# 
fd = str.find("b",0,len(str)) 
print(fd,"find()")

# --- str.rfind(sub, start, end) 和find()功能类似 但是是从右往左查找
# 
fd = str.rfind("b",0,len(str));
print(fd,"rfind()")

# --- str.index(sub, start, end)index()功能find()类似 
# 区别在于index() 如果没有找到直接报错substring not found
# 
index = str.index("b",0,len(str));
print(index,"index()")

# --- rindex()同上 从右到左查找
#
index = str.rindex("b",0,len(str))
print(index,"rindex()")

# --- count(str,start = 0, end = len(str)) 查看区间内某个字符串出现的次数
# 
count = str.count("b",0,len(str))
print(count,"count()")

# *************************** 转换类 **************************
#
# --- str.replace("str",new[,count]) 替换规定的字符串 count规定替换次数为可选
# 并不会对原字符转产生改变
# 
print(str.replace("b","k",2),"replace()")

# --- str.capitalize() 将字符串的首字母变大写 不会影响到原字符串
# 
print(str.capitalize(),"capijtalize()")
print(str)

# --- str.title()将字符串的每个单词的首字母转换为大写字母 不会改变原字符串
str = "hello word"
print(str.title(),"title()")
print(str)

# --- str.lower()将字符串的每个字母都转换为小写 并不影响原字符串
str = "ADASF SDFasd kjk1A"
print(str.lower(),"lower()")
print(str)

# --- str.upper()将字符串的每个字母都转换为大写，并影响到原来的字符

print(str.upper())
print(str)

# ############################ 填充压缩 和清除空格 #############################
# 
# 
# --- str.ljust(width, fillchar)填充字符 width为规定字符的宽度
# 1.0 fillchar 规定填充的字符 必须填充的的是单个字符
# 2.0 如果字符小于宽度 就会把填充字符,填充在字符串的右边
# 3.0 不会影响到原字符的

str = "abcd"
print(str.ljust(8,"x"),"ljust()")
print(str)

# --- str.rjust(width, fillchar) 同上 区别是：会把填充字符 填充到字符串的左边
#
print(str.rjust(8,"x"),"rjust()")
print(str)

# --- str.center(width, fillchar) 功能同上 区别是：字符会填充在字符串的左右两边 如果不平均则左边多一些
# 
print(str.center(7,"x"),"center()")
print(str)

# --- str.strip(chars) 清楚字符串两边空格 或者清除左右两边指定的字符集
#1.0 如果没有规定参数 则清除字符串两边的空格否则清楚规定的字符
#2.0 如果没有找到则返回原字符串

str =" ---a--s--d--f--- "
print("|" + str.strip(" -") + "|","strip()")
print(str)

# --- str.lstrip(chars) 清楚左边的空格或者规定的chars
# 1.0 用法同上 区别是清除字符串左边的空格
# 
print("|" + str.lstrip(" -") + "|","lstrip()")
print(str)

# --- str.rstrip(chars) 清楚右边的空格或者规定的chars
# 2.0 用法同上 区别清楚字符串右边的空格
# 
print("|" + str.rstrip(" -") + "|","rstrip()")
print(str)

# str.zfill(width)在字符的左边填充0
print(str.zfill(30),"zfill()")

# *************************** 分割和拼接 ***************************
# 
str = "asdf-\n4sdf\r-ssdf\s-123-456789"
# --- str.split(sep, maxsplit)
# 1.0 sep以指定的字符 进行分割为列表
# 2.0 maxsplit分割次数 大于次数后面的不会进行分割
# 
print(str.split("-",3),"split()")
print(str)

# --- str.splitlines(keepends)
# 1.0 根据字符串里的空白符号自动进行分割 返回把分割的每一部分插入数组
# 2.0 keepends 是否保留换行符 True为保留
print(str.splitlines(True),"splitlines(True)")

# --- str.partition(sep) 从左边开始检索分割字符，
# 1.0 然后把字符串分割成三部分的元组("sep左侧字符串","sep","sep右侧字符串")
# 2.0 如果没有检索到分割字符 分为三部分的元组("原字符","","")
print(str.partition("-"),"partition()");
print(str.partition("|"))
print(str)


# --- str.rpartition(sep)同上 区别是从右边检索分割字符
print(str.rpartition("-"),"rpartition()");
print(str.rpartition("|"),"rpartition()")


# --- str.join(iterable) 把可迭代的对象用指定的字符拼接起来,变为字符串
arr = ["sdf","妈的生物反馈","465"]
print("**".join(arr),"join()")


# ******************************  字符串的判定或者验证 *************************************
# 
 
# --- inslnum()检查是否是数字或者字母 不可以是字母和数字以外的任何字符包括空和空格 
# 
str = "123asdf"
print(str.isalnum(),"isalnum()")

# --- isalpha()验证字符串是否是全字母 不可以字母以外的字符包括空格和空
# 
str = "asdfasdASDF"
print(str.isalpha(),"isalpha()")

# --- str.isdigit()验证字符串是全数字 不可以是数字意外的任何字符包括空和空格
# 
str = "123"
print(str.isdigit(),"isdigit()")

str = "\n\r\f  "
# --- str.isspace()验证字符串是否都是空格或者空符号 不可以是空字符以外的所有字符
# 
print(str.isspace(),"isspace()")

# --- str.startswith(prefix, start, end)验证一个字符串是否是以规定的字符开头
#  1.0 start规定开头位置 
#  2.0 end规定结束位置 ，不包括结束位置
#
str = "2018bbcc112aabbcc.jpeg"
print(str.startswith("18",2,4),"startswith()") 

# --- str.endswith(suffix, start, end)验证一个字符串是否是以规定的字符结尾的
print(str.endswith(".jpeg"),"endswith()")

# ############################ in and not in ###############################
# 
# --- in 判定一个字符串是否包含另一个字符串
str = 'abcd'
str1 = 'd'
print(str1 in str)

# --- not in 判断一个字符串是否不包含另一个字符串
# 
print("aa" not in "aabb")








