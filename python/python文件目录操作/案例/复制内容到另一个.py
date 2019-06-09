import os
# 1.0 打开文件 和 创建另一个文件 
#     把
get_dir = open("../test/test.txt","r",encoding = "utf-8")
if not(os.path.isfile("test/txt")):
    os.remove("test/txt/copy.txt")
    os.removedirs("test/txt/")
os.makedirs("test/txt",0o444)
# os.F_OK: 检查文件是否存在;

# os.R_OK: 检查文件是否可读;

# os.W_OK: 检查文件是否可以写入;

# os.X_OK: 检查文件是否可以执行
if os.access("test/txt/",os.F_OK):
    print("存在")
else:
    print("文件不存在")
if os.access("test/txt/",os.R_OK):
    print("可读")
else:
    print("文件不可读")
if os.access("test/txt/",os.W_OK):
    print("可以写入")
else:
    print("不可以写入")
if os.access("test/txt/",os.X_OK):
    print("可执行")
else:
    print("不可执行")
set_dir = open("test/txt/copy.txt","a",encoding = "utf-8")

# 2.0  读取文件 

if get_dir.readable():
    if set_dir.writable():
        # 如果文件比较大一次性的读取完毕可能会 崩溃
        # 所以就把他分批次的读取
        while True:
            content = get_dir.read(1024)
            # 如果content 的长度等于0 说明已经读取到最后 可以跳出
            if len(content) == 0:
                break
            set_dir.write(content)
    else:
        print("您没有写入文件的权限")
else:
    print("您读取的文件没有，读取权限")


# 3.0 写入文件
    
# 
# 4.0 关闭文件
set_dir.close()
get_dir.close()