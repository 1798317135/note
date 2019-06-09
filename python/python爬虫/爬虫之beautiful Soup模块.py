from bs4 import BeautifulSoup
html_doc = """
<html><head><title class = 'tit hhe'>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 你好
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">
    <p>
        <a></a>
    </p>
</p>
"""

soup = BeautifulSoup(html_doc, 'lxml')
# --- prettify() 格式化输出
# print(soup.prettify())

# --- soup.get_text() 获取文档全部的文字内容
# print(soup.get_text())

# dom = soup.title
# print(soup)
# 
# ################################### 三大大对象类型 #############################
# 
# ******************Tag 类型 
# 
# --- Tag 对象与XML或HTML原生文档中的tag相同:
print('title type:',type(soup.title),soup.title)
# --- 每个tag都有自己的名字,通过 .name 来获取:
print('name type:',type(soup.title.name),soup.title.name)
# --- 一个tag可能有很多个属性. tag <b class="boldest"> 
#      有一个 “class” 的属性,值为 “boldest” . tag的属性的操作方法与字典相同:
#      可以增删该查
#      多值属性：class 等等 返回的是一个列表list类型
print('attr type:',type(soup.title.attrs),soup.title.attrs)
# --- 将tag转换成字符串时,多值属性会合并为一个值
soup.title['class'] = ['tit','le']
print('string attrs',soup.title)

# ***************** NavigableString 可以遍历的字符串 类型
# 
# 1.0  NavigableString 类来包装tag中的字符串
# 
# --- soup.string 可以去除 tab里面的字符串
print(soup.title.string)

# --- tag中包含的字符串不能编辑,但是可以被替换成其它的字符串,用 replace_with() 方法:
soup.title.string.replace_with("asdf")
print(soup.title.string)

# --- encode() 将字符串 转换成字节
print('adf'.encode().decode())
print(type('adf'.encode()))
print(soup.name)


# ********************* Comment 对象是一个特殊类型的 NavigableString 对象:
# 
markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup)
comment = soup.b.string
print(type(comment))
print(comment)
print(soup.b.prettify())


################################### 子节点 #################################
#
# 一个tag对象 可以能还有内部还包含这 tag 和 string 这些都是她的子节点
# --- 操作子节点 最简单的方法就是 指定tag的name 
#     通常取到的都是第一个指定name 的子节点
#     
#     
soup = BeautifulSoup(html_doc)
# print(soup.p)

# --- 如果想获得所有指定 name 的子节点 需要用到find_all()这个方法
#     他返回这个指定 name 的所有字节点 包括内层嵌套 的指定 name 的子节点
#     
# print(soup.find_all('p'))

# --- tag的 .contents 属性可以将tag内部的所有子节点以列表的方式输出:
# print(soup.contents)

# --- BeautifulSoup 对象本身一定会包含子节点,也就是说<html>标签也是 BeautifulSoup 对象的子节点:

# print(soup.contents[0].name)

# print(soup.p.b.contents)

# --- 通过tag的 .children 生成器,可以对tag的子节点进行循环:
print('-'*5)
# for x in soup.children:
    # print(x)

# --- .descendants 属性可以对所有tag的子孙节点进行递归循环 :
# for x in soup.descendants:
    # print(x)
    
# --- .string
#   如果tag只有一个 NavigableString 类型子节点,那么这个tag可以使用 .string 得到子节点:
#   或者
#   如果一个tag仅有一个子节点,那么这个tag也可以使用 .string 方法,输出结果与当前唯一子节点的 .string 结果相同:
print(soup.p.string)
print('-'*5)
# --- 如果tag中包含多个字符串 [2] ,可以使用 .strings 来循环获取:
#     输出的字符串中可能包含了很多空格或空行,使用 .stripped_strings 可以去除多余空白内容:
# for x in soup.stripped_strings:
    # print(repr(x).replace(r'\n',''))

################################### 父节点 ####################################
#
# --- 通过 .parent 属性来获取某个元素的父节点
#     html 的父节点是 BeautifulSoup
# print(soup.p.contents[0].parent)
# print(type(soup.html.parent))
# 
# --- 通过元素的 .parents 属性可以递归得到元素的所有父辈节点
# for x in soup.a.parents:
#     if x is None:
#         print(x)
#     else:
#         print(x.name)  

################################ 兄弟节点 #######################################
#
# --- 在文档树中,使用 .next_sibling 和 .previous_sibling 属性来查询兄弟节点:
#pri
for a in soup.find_all('a'):
    try:
        print(a.attrs['href'])
    except Exception as e:
        pass