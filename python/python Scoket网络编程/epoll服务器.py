import select
import socket
import re
import queue


def recv_data(data_recv,new_socket):
    
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

    return file_name

def send_data(file_name,client):
    print(file_name)
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

# 创建TCP套接字
tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 设置套接字ip复用
tcp_socket.setblocking(False)

# 设置套接字为非堵塞
tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 绑定服务器端口
tcp_socket.bind(("127.0.0.1",8080))

# 监听客户端 设置最大连接数
tcp_socket.listen(128)

# 定义超时时间
timeout = 100

# 创建epoll对象
epl = select.epoll()

# 注册服务器 等待读事件集合
epl.register(tcp_socket.fileno(),select.EPOLLIN)

# 保存客户端消息的字典
msg_dict = dict()

# 文件描述符 对应 套接字的字典
fd_event_dict = {tcp_socket.fileno():tcp_socket}

while True:
    print("等待客户端的连接")

    # 设置检测客户端的超时时间
    # 并在时间内返回一个数组 每个元素是一个元祖 （fd,evnet）
    # 如果在时间内没有 活动链接 返回空
    fd_event = epl.poll(timeout)
    
    #如果在超时时间内 没有活动连接，从新轮询
    if not fd_event:
        print("没有活动连接，从新轮询")
        continue

    # 这里说明有活动连接
    print("有活动链接,这个活动链接是:{}".format(fd_event))

    # 遍历这个列表的，拆包出fd 和 evnet
    for fd,event in fd_event:
        # 第一个肯定是总套接字的接收到了新的客户端所以这个fd取出的是总套接字tcp_socket
        socket = fd_event_dict[fd]

        # 这个活动链接的文件，是否是总套接字的
        if socket == tcp_socket:

            #那么就代表有新客户端有新的链接
            new_socket,addr = tcp_socket.accept()

            # 然后把这个新的客户端也设置为非堵塞
            new_socket.setblocking(False)

            # 注册新客户端，为可读事件
            epl.register(new_socket.fileno(),select.EPOLLIN)

            # 并且把这个新的客户端和文件描述符粗存到字典当中 以便上下文使用
            fd_event_dict[new_socket.fileno()] = new_socket

            # 并且把这个客户端信息 和对应的储存客户端信息的队列储存到字典
            msg_dict[new_socket] = queue.Queue()

        # 客户端异常关闭事件  
        elif event & select.EPOLLHUP:
            # 这个说明有客户端关闭列链接
            print("客户端异常关闭！")

            # 然后把这个客户端给注销了
            epl.unregister(fd)

            # 关闭这个客户端
            fd_event_dict[fd].close()

            # 把他从字典中删除
            del fd_event_dict[fd]

            # 删除他的消息缓存
            del msg_dict[socket]

        # 可读事件
        elif event & select.EPOLLIN:
            # 连接数据
            data = socket.recv(1024)

            # 判断是否时客户断开连接
            if data:
                 # 处理数据
                file_name = recv_data(data,socket)

                # 处理过的数据放到对应的列队当中
                msg_dict[socket].put_nowait(file_name)

                # 改变这个客户端的事件状态为可写
                epl.modify(fd,select.EPOLLOUT)
            else:
                # 这个说明有客户端关闭列链接
                print("客端关闭了浏览器")

                # 然后把这个客户端给注销了
                epl.unregister(fd)

                # 关闭这个客户端
                fd_event_dict[fd].close()

                # 把他从字典中删除
                del fd_event_dict[fd]

                # 删除他的消息缓存
                del msg_dict[socket]

        # 可写
        elif event & select.EPOLLOUT:
            try:
                # 从队列中获取请求的数据
                file = msg_dict[socket].get_nowait()
            except queue.Empty:
                epl.modify(fd, select.EPOLLIN)
            else:
                # 发送数据
                send_data(file,fd_event_dict[fd])
        else:
            pass

# 销毁
epl.unregister(tcp_socket.fileno()) 

# 关闭epll
epl.close()

#关闭总套接字
tcp_socket.close()