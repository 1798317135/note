#  UDP没有TCP的握手、确认、窗口、重传、拥塞控制等机制，
#  UDP是一个无状态的传输协议
#  
#  1.0 创建一个socket 套接字对象
import socket
import time
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
# with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
#     # 2.0 可以使用套接字来收发数据
#         # 发送UDP数据，将数据发送到套接字，address是形式为（ipaddr，port）的元组，
#         # 指定远程地址。返回值是发送的字节数。
#     port = int(input("对方的port:"))
#     addr = ("",port)
#     print(addr)
#     # 3.0 给套接字绑定端口号
#     #     如果不绑定的话，系统回自动分配一个动态端口号
#     #     这就造成每一次发送出去的源端口，都不一样
#     #     注意同一个端口在同一时间只能用一次
#     #     
#     # s.bind(("",2246))
#     while True:
#         data = input("请输入发送的数据：")
#         data_time = "{}\n{}".format(time.ctime(),data)
#         s.sendto(data_time.encode("utf-8"),("192.168.1.4",port))
#         data,addr = s.recvfrom(1024)
#         print(data.decode("utf-8"))
def recv_msg(udp_socket):
    while True:
        data,addr = udp_socket.recvfrom(1024)
        print("\n接收到的消息是:\n{}\n发送消息:".format(data.decode("utf-8")))

def send_msg(udp_socket,dest_port):
    while True:
        send_data = input("\n发送消息:")
        udp_socket.sendto(send_data.encode("utf-8"),("192.168.1.4",dest_port))

def main():
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_socket.bind(("",3375))
    dest_port = int(input("对方的port"))
    with ThreadPoolExecutor(max_workers = 5) as thread_pool:
        thread_pool.submit(recv_msg,udp_socket)
        thread_pool.submit(send_msg,udp_socket,dest_port)


if __name__ == '__main__':
    main()