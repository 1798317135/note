############# XPath简介

# XPath 使用路径表达式在 XML 文档中进行导航
# XPath 包含一个标准函数库
# XPath 是 XSLT 中的主要元素
# XPath 是一个 W3C 标准
# 
# ########### 语法
# 
# bookstore 选取 bookstore 元素的所有子节点。
# 
#/bookstore 
#   -- 选取根元素 bookstore。
#   -- 注释：假如路径起始于正斜杠( / ),则此路径始终代表到某元素的绝对路径！
# 
# bookstore/book    选取属于 bookstore 的子元素的所有 book 元素。
# 
# //book    选取所有 book子元素，而不管它们在文档中的位置。
# 
# bookstore//book  选择属于 bookstore 元素的后代的所有 book 元素，而不管它们位于 bookstore 之下的什么位置。
# 
# //@lang   选取名为 属性有lang。
# 
# ########### 选区特定节点
# 
# /bookstore/book[1]    选取属于 bookstore 子元素的第一个 book 元素。
# 
# /bookstore/book[last()]   选取属于 bookstore 子元素的最后一个 book 元素。
# 
# /bookstore/book[last()-1] 选取属于 bookstore 子元素的倒数第二个 book 元素。
# 
# /bookstore/book[position()<3] 选取最前面的两个属于 bookstore 元素的子元素的 book 元素。
# 
# //title[@lang]    选取所有拥有名为 lang 的属性的 title 元素。
# 
# //title[@lang='eng']  选取所有 title 元素，且这些元素拥有值为 eng 的 lang 属性。
# 
# /bookstore/book[price>35.00]  选取 bookstore 元素的所有 book 元素，且其中的 price 元素的值须大于 35.00。
# 
#bookstore/book[price>35.00]/title  选取 bookstore 元素中的 book 元素的所有 title 元素，且其中的 price 元素的值须大于 35.00。 

# /bookstore/*  选取 bookstore 元素的所有子元素。
# 
# @*  匹配任何属性节点。
# 
# //title[@*]   选取所有带有属性的 title 元素。
# 
# //book/title | //book/price   选取 book 元素的所有 title 和 price 元素。
# 
# //title | //price 选取文档中的所有 title 和 price 元素。
# 
# /bookstore/book/title | //price   选取属于 bookstore 元素的 book 元素的所有 title 元素，以及文档中所有的 price 元素。

# /text() 获取文本