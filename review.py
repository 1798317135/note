######################### ubuntu复习 ###############################
# ************ 8.2 号
# ------ 基本常识
# / 根目录
# /root 超级管理员目录 系统文件所在目录
# /boot 系统启动文件目录
# /bin 存放二进制文件
# /sbin 存放系统二进制文件
# /etc 存放系统配置文件
# /dev 存放设备有关的文件 驱动等 
# /home 用户目录 存放每个用户的个人数据 除了root用户
# /tmp 临时文件目录
# /usr 存放个人的程序和配置文件等 apt 工具会管理这个目录
# /usr/bin 存放个人程序
# /usr/sbin 存放超级管理的管理层序
# /usr/share 存放共享数据
# /usr/lib 存放程序的函数库文件
# /usr/local 存放手动安装的软件 里面有usr同样的目录结构 
# /usr/src 用户存放下载的安装包等
# /opt 存放实验的程序 安装到此目录的程序和配置文件会在统一文件下

# ～ 用户的家目录
# . 开头的文件是隐藏文件
# . 当前目录
# .. 上级目录
# - 可以用cd 在最近使用的两个文件夹切换
# ./文件 执行文件
# 
#shutdown 关闭或者重启电脑
#	-r 重新启动 now 现在关闭

# pwd 查看当前路径

# who 查看当前登陆的用户列表
# whoami 查看当前登陆的用户
# whicth 查看执行程序所在的目录路径
# exit 退出用户
# su 用户名 切换用户不切换当前用户
# su - 用户名 切换用户并且切换到当前目录的家目录
# su 切换到超级管理员用户
# top 查看cpu的使用情况
# ps -aux 查看进程的详细信息
# date 查看时间
# cal -y 查看日历
# 
# 

# ls 查看文件夹目录
# 	-a 显示隐藏文件
# 	-l 列表的方式显示
# 	-h 现实文件大小
# 	* 任意字符 任意长度
# 	？ 单个字符
# 	【】匹配其中的任意一个字符

# touch 创建文件 如果存在修改日期

# mkdir 创建目录 
# 	-p 第归创建目录

# rm 删除文件
# 	-r 删除目录
#   -f 强制删除不提示

# tree 树桩图结构目录
# 	-d 之显示目录
# 	-f 之显示文件

# cp 复制民命令
# 	-i 覆盖提示
# 	-r 复制目录

# mv 移动文件或者目录 可以改名
# 	-ℹ 覆盖提示

# cat 查看文件内容
# 	-n 显示所有行的行号
# 	-b 不显示空行的行号

# more 分批查看文件内容

# grep 搜索文本
# 	-n 显示搜索的行号
# 	-v 显示其他

# ssh -p 22 user@122.117.135 远程连接
# 	-p 端口号
# 
# scp -P 22 本地文件 user@127.4154.45:远程路径 
# scp -P 22 -r user@127.0.0.1：远程目录 本地路径
# 	-r 如果复制文件

# d 代表目录 -代表为文件
# r 可读权限 x 可执行权限 w 可写权限
# chmod -R 777 文件/目录 来增加或者减少文件目录的权限
# chown -R user：group 文件或目录 修改文件或这么目录的拥有者
# chgrod -R 祖名 文件/或者目录 修改文集和目录的组


# sudo groupadd 组名 添加组
# cat etc/group 确认组
# sudo groupdel 组名 删除组
# sudo groups 用户名 看看用户加入的所有组
# sudo gpasswd -a user group 添加用户到指定组
# sudo gpasswd -d user group 移除组里面的指定用户

# sudo useradd -m -g 所属组 用户名  创建用户 -m 会创建用户的家目录
# sudo passwd 用户名 给新用户设置密码
# cat /etc/passwd 储存的是用户信息 
# sudo  userdel 用户名 删除用户

# sudo usermod -g 主组 用户名 修改用户的主组
# sudo usermod -G 用户名 添加用户的附加组
# sudo usermod -s /bin/bash 用户名 添加用户的shell窗口类型
# sudo userdel -rf 强制删除用户和用户的家目录

# find 文件路径 -name 文件 在制定目录下查找指定文件

# ln -s 源文件（绝对路径） 阮连接路径 建立一个文件的快捷方式
# ln 源文件 硬链接地质 建立一个文件名的复制 

# tar -vcf *.tar 创建一个tar包
# tar -xcf 包名 解开一个tar包
# tar -zvcf *.tar.gz 创建一gzip压缩的tar包
# tar -jcvf *.tar.zb2 
# tar -jzvf 

# vim 
# 末尾模式 
# x  保存退出
# q  退出
# w  保存
# ！ 强制执行

# 编辑模式
# i 光标移动到字符前面
# I 光标移动行首
# a 移动到字符后面
# A 光标移动到行未
# o 光标下面创建一个空行
# O 光标在上面创建一个空行




# dd 删除光标所在行
# yy 复制
# p  粘贴

# vim file +: 打开文件并且光标在第一行
# vim file +  打开文件并且光标在末行
# vim file +/.. 打开文件光标移动到查找到字符的行
# vim -o file1 file2 file3  分屏显示多个文件


# gg 光标跳到文件首部
# G 光标跳到文件尾部尾
# 0 光标移动到行首
# $ 光标移动到行第一个非空白字符
# ^ 光标移动到行的最后一个空白字符

# w 向后面移动
# b 向前
# e 向后移动一个单词的距离

# shift + >> 向

# /sdf\c 查找字符 \c是不分大小写
# * 可以快速查找光标的单词
# /%s/查找字符/替换字符/gc 全部查找替换 c确认



########################## git #################

# git init 初始化仓库
# git status 查看状态
# git add * 跟踪文件和提交文件到暂存
# git rm -r 删除本地文件
# git rm -r --cached 删除工作区 不删除文件
# git checkout -- file 撤销工作区的改动
# git reset HEAD file 撤销缓存区
# git commit -a -m '1.0.0' 创建版本库
# git commit --amend -m 重新提交
# git reset --hard HEAD~1 回退到第一个版本
# git reset --hard tab或者hash
# git deff HEAD HADE^ -- 文件 对比这个版本和上一版本的区别
# git tag -a -m '辅助标签'
# git tag '轻量级标签'
# git tab 查看标签
# git tab -l 匹配查看标签
# git log 查看提交历史
# git log --pretty=online 每个显示一行
# git log --graph 显示合并路线
# git reflog 查看操作记录
# git branch 查看分支
# git barnch -a 查看远程分支
# git barnch -v 查看此分支
# git branch -d 删除分支
# git branch -vv 查看分支和提交历史
# git branch --delete 删除远程分支
# git checkout -b 创建并切换到分支
# git checkout -d
# git merge 合并分支
# git merge --no-ff -m 强制自动合并
# git remote -v 查看远程仓库
# git remote add url 添加远程仓库
# git remote fetch 拉取远程仓库
# git remote push 推送本地仓库
# git remote rename 修改远程仓库名字
# git remote pull 拉去远程并合并
#

