import socket
from concurrent.futures import ProcessPoolExecutor
import concurrent.futures
from threading import Thread
import re,time
# import gevent,time
# from gevent import monkey
# monkey.patch_all()

# class Tcp_gevent:
#     def __init__(self,new_client):
#         self.new_client = new_client
#         self.file_name = None

#     def recv(self):
#         # 1.0 接收用户请求
#         rquests_data = self.new_client.recv(1024).decode("utf-8")

#         # 2.0 解析用户请求信息
#         response_lines = rquests_data.splitlines()
#         pattern = re.compile(r"[^/]/(?:([.*?/]?.+\.(?!map)[a-zA-Z]+)\d?.*\s)?(?:[^ ]*)?")
#         m = pattern.search(response_lines[0])
#         if m:
#             self.file_name = m.group(1)
#             if m.group() == " /":
#                 self.file_name = "/index.html"
#         return self.file_name

#     def send(self):
#         # 2.0 返回给新用户返回数据
#         # 2.1 设置状态行
#         time.sleep(1)
#         response_header = "HTTP/ 200 OK\r\n"
#         response_header += "\r\n"
#         # 2.0 设置响应体
#         # print(file_name)
#         try:
#             f = open("moban3382/{}".format(self.file_name.lstrip()),"rb")
#         except Exception as e:
#             print(e)
#             response_header = "HTTP/ 404 NOT FOUND\r\n"
#             response_header += "\r\n"
#             response_header += "---- file not found---"
#             new_client.send(response_header.encode("utf-8"))
#         else:
#             response_body = f.read()
#             f.close()

#             # 返回响应状态行 和 消息头
#             self.new_client.send(response_header.encode("utf-8"))

#             # 返回响应内容
#             self.new_client.send(response_body)

#     def __call__(self):
#         print(12)
#         gevent.joinall([
#             gevent.spawn(self.recv),
#             gevent.spawn(self.send),
#             ])

    


class Tcp_thread(Thread):

    def __init__(self,new_client):
        super().__init__()
        self.new_client = new_client
        self.file_name = None

    def run(self):
        self.recv()
        self.send()
        self.new_client.close()        

    def recv(self):
        # 1.0 接收用户请求
        rquests_data = self.new_client.recv(1024).decode("utf-8")

        # 2.0 解析用户请求信息
        response_lines = rquests_data.splitlines()
        pattern = re.compile(r"[^/]/(?:([.*?/]?.+\.(?!map)[a-zA-Z]+)\d?.*\s)?(?:[^ ]*)?")
        m = pattern.search(response_lines[0])
        if m:
            self.file_name = m.group(1)
            if m.group() == " /":
                self.file_name = "/index.html"
        return self.file_name

    def send(self):
        # 2.0 返回给新用户返回数据
        # 2.1 设置状态行
        response_header = "HTTP/ 200 OK\r\n"
        response_header += "\r\n"
        # 2.0 设置响应体
        # print(file_name)
        try:
            f = open("moban3382/{}".format(self.file_name.lstrip()),"rb")
        except Exception as e:
            print(e)
            response_header = "HTTP/ 404 NOT FOUND\r\n"
            response_header += "\r\n"
            response_header += "---- file not found---"
            new_client.send(response_header.encode("utf-8"))
        else:
            response_body = f.read()
            f.close()

            # 返回响应状态行 和 消息头
            self.new_client.send(response_header.encode("utf-8"))

            # 返回响应内容
            self.new_client.send(response_body)

    def __call__(self):
        self.start()

    # def __del__(self):
    #     print("关闭")
        # self.new_client.close()


def main():
    """
    主程序
    """
    # 1.0 创建TCP套接字对象
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as tcp_sockt:

        # 2.0 设置套接字
        tcp_sockt.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

        # 3.0 绑定地址和端口
        addr = ("127.0.0.1",8080)
        tcp_sockt.bind(addr)

        # 4.0 被动监听客户端连接
        tcp_sockt.listen(128)
        with ProcessPoolExecutor() as p:
            start = time.clock()
            while True:
                
                # 5.0 接收新用户
                new_clint,addr = tcp_sockt.accept()

                #  实例化一个多线程的用户处理对象
                recv_client = Tcp_thread(new_clint)
                # recv_client = Tcp_gevent(new_clint)
                p.submit(recv_client())
                end = time.clock()
                print("执行时间{}".format(end-start))

if __name__ == '__main__':
    main()
