import socket
import sys,time
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

class Socket_UDP:
    """
    scoket_udp通信
    接收和发送信息
    """

    def __init__(self,addr,socket_obj):
        self.socket_obj = socket_obj
        self.socket_obj.bind(addr)
        self.sour_addr = None

    def recv_msg(self):
        """接收信息return 返回发送者的地址和端口元祖"""

        while True:
            # 1.0 阻塞接收消息
            msg = self.socket_obj.recvfrom(1024)
            # 2.0 拆包
            data,addr = msg
            # 3.0 打印完整消息
            print("网名:{}\n请输入发送消息:".format(str(addr[0]),data.decode("utf-8")))
            # 4.0 返发送者的信息元祖
            self.sour_addr = addr

    def send_msg(self):
        """发送消息"""
        while True:
            # 1.0 获取时间元祖
            tuple_time = time.localtime()
            # 2.0 把时间元祖格式化
            data_times = time.strftime("%H:%I:%M %S",tuple_time)
            # 3.0 获取发送的字符
            data = input("\n请输入发送的数据：")
            # 4.0 拼接完整的数据
            whole_data = "{}\n{}".format(data_times,data)
            # 5.0 发送消息到接收到的
            self.socket_obj.sendto(whole_data.encode("utf-8"),self.sour_addr)

    def __del__(self):
        self.socket_obj.close()

def main():
    # 创建 socket 对象
    socket_obj = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    port = int(input("绑定端口:"))
    addr = ("",port)
    s = Socket_UDP(addr,socket_obj)
    with ThreadPoolExecutor(max_workers = 5) as thread_pool:
        thread_pool.submit(s.send_msg)
        thread_pool.submit(s.recv_msg)

if __name__ == '__main__':
    main()
