# 1.0 sudo apt update
# 2.0 sudo apt install redis-server
# 
# *******启动Redis
# redis-server

# ******** 配置
# sudo redis-server /etc/redis/redis.conf
# 
# ******* 查看是否启动
# redis-cli
# 
# ####### 获取所有配置项
# 
# --- CONFIG GET *
# 
# --- CONFIG SET xxx 来实设置响应的配置
# 
# 
# ############################## windown 安装
# 
# 1.0 下载路径
#     https://github.com/MSOpenTech/redis/releases。
# 
# 2.0 点击msi 安装，一般选项默认
#
# 3.0 初始化启动
#     redis-server.exe redis.windows.conf
# 
# 4.0 测试
#      set mykey 1321
#      get mykey 
# 5.0 打开关闭服务，并且手动把服务设置为手动
#      net start redis
#      net stop redis