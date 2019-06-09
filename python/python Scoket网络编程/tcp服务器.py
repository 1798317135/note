import socket
import sys
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import gevent,time
from gevent import monkey

# def client_ac(socket_obj):
#     while True:
#         client,addr = socket_obj.accept()
#         print("已经建立连接,客户端地址为{}".format(str(addr)))
#         msg = input("发送什么")
#         client.send(msg.encode("utf-8")) # 发送到源客户端
#         break

# def main():
#     # 1.0 创建套接字对象
#     with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
#         # 2.0 绑定端口号
#         host = socket.gethostname() # 获取本地主机名 
#         port = 9980 # 设置端口  
#         s.bind((host,port))
#         # 3.0 设置监听连接设置最大连接数
#         s.listen(5)
#         # 创建线程池
#         monkey.patch_all()
#         gevent.joinall([
#             gevent.spawn(client_ac,s),
#             gevent.spawn(client_ac,s),
#             gevent.spawn(client_ac,s),
#             gevent.spawn(client_ac,s),
#             gevent.spawn(client_ac,s),
#             ])
#         # while True:
#         #     # 4.0 建立客户端连接 
#         #     client,addr = s.accept()
#         #     print("已经建立连接,客户端地址为{}".format(str(addr)))
#         #     # print(client,addr)
#         #     # 5.0 发送数据
#         #     msg = "欢迎连接服务器\n"
#         #     client.send(msg.encode("utf-8")) # 发送到源客户端
        
import os,json
import gevent
from gevent import monkey
# if __name__ == '__main__':
#     main()
def udp_server():
    with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as udp_socket:
        # 1.0 绑定服务地址
        addr = ("",9955)
        udp_socket.bind(addr)
        # 2.0 获取文件列表
        file_list = os.listdir("../../html5/images/")
        json_file_list = json.dumps(file_list)
        # 2.0 非阻阻塞接收客户端
        while True:
            data,addr = udp_socket.recvfrom(1024)
            if data.decode("utf-8") == "loolfilelist":
                # 返回列表
                udp_socket.sendto(bytes(json_file_list,encoding = "utf-8"), addr)


def tcp_server():
    addr = (socket.gethostname(),2255)
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_socket.bind(addr)
    file_list = os.listdir("../../html5/images/")
    os.chdir("../../html5/images/")
    tcp_socket.listen(128)
    while True:
        new_client,addr = tcp_socket.accept()
        data = new_client.recv(1024)
        data = data.decode("utf-8")
        if data in file_list:
            f = open(data,"rb")
            while True:
                img = f.read(1024)
                new_client.send(img)
                if img == "":
                    break
        new_client.close()
    f.close()
    tcp_socket.close()

def main():
    # 1.0 创建一个udp的套接字对象专门，返回文件列表

    monkey.patch_all()
    gevent.joinall([
        gevent.spawn(tcp_server),
        gevent.spawn(udp_server),
        ])
    
if __name__ == '__main__':
    main()