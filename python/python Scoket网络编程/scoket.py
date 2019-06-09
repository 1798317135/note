# --- socket 可以完成网络通信
#     socket 简称为套接字
#     套接字是响应网络请求和发送网络请求
#     主要包括
#     best ip --- 目标ip
#     best sport --- 目标端口
#     src ip --- 源ip
#     src sport --- 源端口
#      
#     socket的使用格式比较固定
#     主要分为三步
#     1 创建
#     2 收发数据
#       socket 创建出来的套接字是全双工
#       也就是同一个套接字即可以收也可以发
#       
#     3 关闭
#     可以直接使用whit 语句
# socket.socket（family = AF_INET，type = SOCK_STREAM，proto = 0，fileno = None ）
# socket.AF_INET ipv4
# socket.AF_INET6 ipv6
# SOCK_STREAM TCP 面向链接的传输协议
# SOCK_DGRAM UDP 无状态的传输协议

import socket
# # 创建socket 对象

# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# # 使用 收发数据
# # 
# s.sendto() #发数据
# #
# #关闭
# s.close()
with socket.socket(socket.AF_INET ,socket.SOCK_DGRAM) as s:
    print(s)

