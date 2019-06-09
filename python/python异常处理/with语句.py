# 1.0 with context_expression[as target(s)]:
#               with body
# 2.0 with 语句给 在执行 某段代码 的是时候 先执行 上下文管理器 as 后面接收到 上下文管理器
#     __enter__方法 返回的 值
#     
#     然后执行with 代码块
#     
#     无论代码块是否报错 都会 调用 __exit__方法
#     上下文管理器的 __exit__ 可以自动 关闭文件 
#     不用 自己关闭


# with open("img/12.jpg","r",) as x:
#     content = x.read()
# # --- file.fileno() 返回一个整形的文件描述 
#     print(x.fileno())
# # --- file.isatty() 如果连接一个终端返回true
#     print(x.isatty())

################################ with嵌套 ########################################
#
#
with open("../python文件操作/img/12.jpg","rb") as w,open("1.jpeg","wb") as r:
    content = w.read()
    r.write(content)
