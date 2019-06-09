# tcp 是面向连接的通信协议
# tcp 严格区分服务器和客户端
import socket,json,time

def filelist():
    addr = (socket.gethostname(),9955)
    # 0.0 询问是否查看
    ask = int(input("查看请收入 1,不查看随机收入:"))
    if ask != 1:
        return False

    # 1.0 创建udp套接字对象
    with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as dup_socke:
        # 2.0 发送查看文件列表的命令
        data = "loolfilelist"
        dup_socke.sendto(data.encode("utf-8"),addr)
        # 4.0 接收服务器返回的文件列表信息
        msg = dup_socke.recvfrom(1024)
        data,addr = msg
        file_list = json.loads(str(data,encoding = "utf-8"))
        return file_list

def main():
    # 1.0 创建socket套接字对象
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 2.0 连接服务器
    addr = (socket.gethostname(),2255)
    try:
        arror_info = tcp_socket.connect(addr)
    except Exception as e:
        raise e
    # 3.0 是否查看可以下载的所有文件
    rd = filelist()
    if rd:
        print(rd)

    # # 4.0 获取下载的文件名称
    file_name = input("请输入需要下载的文件名字：")

    # # 5.0 发送到服务器
    tcp_socket.send(file_name.encode("utf-8"))
    recv_data = tcp_socket.recv(1024)
    # # 6.0 接收服务器返回数据
    for x in recv_data: 
        # # 7.0 把接收到的数据保存到文件当中
        f = open("[新]"+file_name,"ab")
        f.write(recv_data)
    f.close()

    # # 8.0 关闭套接字对象
    tcp_socket.close()

if __name__ == '__main__':
    main()