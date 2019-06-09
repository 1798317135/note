
############################### 和epoll 相似的方法 和缺点
# --- 非阻塞轮询的弊端
# 1.0 当使用非阻塞轮询的方式的socket 效率很低
#      因为他通过循环轮询的方式来遍历套接字，来达到并发的目的，如果并发大，套接字很多的时候就会循环很长时间，减少了效率
#      如果有的文件并没有 进行I/O操作，还有去遍历的话，cup就会空转
# 
# 2.0 这样的方式 程序和内核之间并没有公用的内存，每次接受新的用户连接，操作系统就会拷贝一份套接字的文件，开销大
# 
# ---- select 
#  1.0 单个进程能够监视的文件描述符有限，32位机默认是1024个。64位机默认是2048.
#  2.0 对于socket 的扫描时通过 轮询的方式 效率低
#  3.0 内核空间和进程空间之间通过拷贝的方式传递。开销大
# 
# --- poll
#  1.0 poll 和 select 缺点基本一致
#  
#  ############################ epoll 
# --- epooll的方式
# 1.0 epoll 采用内核和进程通用一块内存空间，无需拷贝内存
# 2.0 epoll 采用时间通知也就是回调函数的的方式，来通知进程哪个文件描述符比较活跃，无须轮询，增加效率
# 
# 
# ############################# 一般使用步骤
# 
# 1.0 创建1个epoll对象
# 2.0 告诉epoll对象，在指定的socket上监听指定的事件
# 3.0 询问epoll对象，从上次查询以来，哪些socket发生了哪些指定的事件
# 4.0 在这些socket上执行一些操作
# 5.0 告诉epoll对象，修改socket列表和（或）事件，并监控
# 6.0 重复步骤3-5，直到完成
# 7.0 销毁epoll对象

############################## 相关的用法
#import select 导入select模块

# epoll = select.epoll() 创建一个epoll对象

# epoll.register(文件句柄,事件类型) 注册要监控的文件句柄和事件

# 事件类型:

# 　　select.EPOLLIN    可读事件

# 　　select.EPOLLOUT   可写事件

# 　　select.EPOLLERR   错误事件

# 　　select.EPOLLHUP   客户端断开事件

# epoll.unregister(文件句柄)   销毁文件句柄

# epoll.poll(timeout)  当文件句柄发生变化，则会以列表的形式主动报告给用户进程,timeout

#                      为超时时间，默认为-1，即一直等待直到文件句柄发生变化，如果指定为1

#                      那么epoll每1秒汇报一次当前文件句柄的变化情况，如果无变化则返回空

# epoll.fileno() 返回epoll的控制文件描述符(Return the epoll control file descriptor)

# epoll.modfiy(fineno,event) fineno为文件描述符 event为事件类型  作用是修改文件描述符所对应的事件

# epoll.fromfd(fileno) 从1个指定的文件描述符创建1个epoll对象

# epoll.close()   关闭epoll对象的控制文件描述符
#
#
############################## 使用场景
#
# 1.0 epoll的性能可能最好，但是在并发少，并且每个套接字都很活跃的情况下，可能 poll 和 select 更加合适
#     因为如果连接数少 轮询的方式未必低，而且如果用户都很活跃的话，减少了 cpu空转，增加性能
#     
import socket
import select,re

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
    # new_client_list = list()


    # 创建一个epoll对象
    epl = select.epoll()

    # 获取套接字的文件描述符
    s_fd = tcp_socket.fileno()

    # 储存x新连接套接字文件描述符和事件的字典
    fd_event_dict = dict()

    # 将监听套接字的文件描述符注册到epoll的内存里面去，第二个参数检测有
    # 输入或者收出，这里需要检测是否有收入EPOLLIN
    # select.EPOLLIN    可读事件
    # select.EPOLLOUT   可写事件
    # select.EPOLLERR   错误事件
    # select.EPOLLHUP   客户端断开事件
    epl.register(s_fd,select.EPOLLIN)

    while True:
        # 堵塞的方式，监听套接字的I/O操作，以时间通知的方式告诉程序，然后解堵塞，
        # 返回一个fd,和event元素组成的列表 有可能式多个套接字可以收了所以式一个列表
        # 储存多个可以进行接收请求的套接字文件描述符
        fd_event_list = epl.poll()

        # 通过遍历的方式 拆包取出每一个可以接收请求的fd，和evevt
        for fd,event in fd_event_list:
            # 判断是取出这个套接字是否是总套接字
            # 可以区分到底是 总套接字接收了 亲用户，还是已经接收的新用户在
            # 进行I/O操作
            if fd == s_fd:
                # 来接收这个可以接收请求的新客户端
                new_client,addr = tcp_socket.accept()
                
                # 并且把新接收的套接字的文件描述符 注册到epoll当中
                epl.register(new_client.fileno(),select.EPOLLIN)

                # 并且把新的客户端写入到字典点当中，fd为key 新套接字为值
                # print(new_client,new_client.fileno())
                fd_event_dict[new_client.fileno()] = new_client

            elif event&event == select.EPOLLIN: #判断如果这个事件存在 并且是可写事件

                # 读取这个请求的数据
                data_recv = fd_event_dict[fd].recv(1024)

                # 判断数据是否为空，为空说明断开连接
                if data_recv:
                    # 处理数据
                    recv_reques(data_recv,fd_event_dict[fd])
                else:
                    #删除这个fd对应的套接字文件
                    del fd_event_dict[fd]

                    # 释放这个文件描述符
                    epl.unregister(fd)
    # 关闭总套接字
    tcp_socket.close()
                    

if __name__ == '__main__':
    main()