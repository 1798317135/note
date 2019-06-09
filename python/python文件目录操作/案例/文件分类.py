import os
import random
import shutil
# 1.0 创建混合文件夹
if not(os.path.isdir("dis")):
    os.mkdir("dis")

# 2.0 修改当前目录
# os.chdir("dis/")

# 3.0 随机生成多种类型文件放入到dis文件里面
    # 3.1 取出文件test文件夹test.txt 里面的文件扩展名
f = open("../test/test.txt","r",encoding="utf-8")
content = f.readlines()
for x in range(len(content)):
    # print(content[x])
    index = content[x].find("：",0)
    content[x] = content[x][0:index]
f.close()


path = "dis/"
#  4.0 修改当前文件
if not os.path.exists(path):
    print("当前文件是不存在的")
    exit()
os.chdir(path)

#  5.0 随机文件名，随机后缀名，插入到文件但中
str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
lens = len(os.listdir())
lon = 0
if lens < 10:
    lon = (30 - lens)
    for x in range(0,lon):
        hz = random.choice(content)
        filename = "%s-%s.%s" % ("".join(random.sample(str,4)),"".join(random.sample(str,4)),hz)
        w = open(filename,"w")
    w.close()

#  6.0 文件分类
#  
l = os.listdir()

#  7.0 遍历所有文件
for x in l:
    if not os.path.isdir(x):
        continue
    # 7.1 获取所有的后缀名
    index = x.rfind(".")
    hz = x[index+1:len(x)]
    
    # 判断此后缀后缀名是否存在文件夹
    if not(os.path.isdir(hz)):
        os.mkdir(hz)

    # 把这个文件移动到对应的文件夹下面
    if not(os.path.isfile(x)):
        shutil.move(x,hz)


    


