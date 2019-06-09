import os
def listFiles(dir,f,t=""):
    # 1.0  列举给文件夹里面的所有文件
    file_list = os.listdir(dir)
    # 2.0 遍历
    for file_name in file_list:
        new_fileName = dir+"/"+file_name
        if os.path.isdir(new_fileName):
            # print(new_fileName)
            f.write(t+new_fileName+"\n")
            listFiles(new_fileName,f,t = "----")
        elif os.path.isfile(new_fileName):
            hz = new_fileName.count("/")
            str = "--" * hz
            if hz>2:
                f.write(str+file_name+"\n")
            elif hz==1:
                f.write("-------------------------------\n")
            else:
                f.write("----"+file_name+"\n")
        print("\n")
f = open("dis/lists.txt","a",encoding ="utf-8")
listFiles("dis",f)
f.close()
import scripy
