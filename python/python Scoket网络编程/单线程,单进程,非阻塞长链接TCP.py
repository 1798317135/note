####################### 非阻塞 I/O轮询的长链接方式TCP
import socket
import re

def recv_reques(data_recv,client):
    """网络I/O操作"""

    # 解析请求头
    request_list = data_recv.decode("utf-8").splitlines()

    # 取出状态行进行正侧提取
    pattern = re.compile(r"[^/]/(?:([.*?/]?.+\.(?!map)[a-zA-Z]+)\d?.*\s)?(?:[^ ]*)?")
    m = pattern.search(request_list[0]) 
    if m:
        file_name = m.group(1)
        if m.group() == " /":
            file_name = "/index.html"
    
    # 如果file_name = / 默认是index.html
    if file_name == " /":
        file_name = "index.html"

    # 打开读取请求文件
    with open("moban3382/{}".format(file_name.strip()),"rb") as f:
        # 响应体
        response_body = f.read()
    # 设置响应报文
    response_header = "HTTP/ 200 OK\r\n"
    response_header += "Connection:keep-alive\r\n" # 保持连接长链接
    response_header += "Content-length:{}\r\n".format(len(response_body)) #设置响应体的长度，如果不设置的话 长链接无法判断数据是否发送完毕
    response_header += "\r\n"

    # 返回数据响应头
    client.send(response_header.encode("utf-8"))
    # 返回响应体
    client.send(response_body)

def main():
    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 设置套接字为
    tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

    # 设置套接字为非阻塞
    tcp_socket.setblocking(False)

    # 服务器绑定地址
    tcp_socket.bind(("127.0.0.1",8080))

    # 监听用户连接
    tcp_socket.listen(128)

    # 储存新用户的数组
    new_client_list = list()

    # while True 解决单线程，非堵塞的高并发
    while True:
        try:
            # 判读是否有用户连接
            new_client,addr = tcp_socket.accept()

        except Exception as e:
            pass
        else:
            # 给这个新用户的recv解堵塞
            new_client.setblocking(False)

            # 有数据的话说明连接成功,把这个用户存到列表
            new_client_list.append(new_client)

        # 遍历这个新用户的列表
        for client in new_client_list:
            try:
                # 判断是否有请求数据
                data_recv = client.recv(1025)
            except Exception as e:
                pass
            else:
                # 判断数据是否为空，为空说明断开连接
                if data_recv:
                    # 处理数据
                    recv_reques(data_recv,client)
                else:
                    #删除数组里面
                    new_client_list.remove(client)
                

    # 关闭总套接字
    
if __name__ == '__main__':
    main()