import socket
import re,os,stat

def service_recv(new_client,addr):
    """
    接收用户，的请求数据

    """
    # 1.0 接收新用户的请求数据
    request_data = new_client.recv(1024).decode("utf-8")
    print(">"*20)

    # 1.1 解析请求头
    response_lines = request_data.splitlines()
    print(response_lines[0])
    #GET /font-awesome-4.7.0/fonts/fontawesome-webfont.woff2?v=4.7.0 HTTP/1.1
    # pattern = re.compile(r"[^/]/([.*?/]?.+\.[a-zA-Z]+).*\s")2?v=4.7.0
    # ('font-awesome-4.7.0/fonts/fontawesome-webfont.woff?v=4.7.0', None, None, None)
    # 
    pattern = re.compile(r"[^/]/(?:([.*?/]?.+\.(?!map)[a-zA-Z]+)\d?.*\s)?(?:[^ ]*)?")
    m = pattern.search(response_lines[0])  
    if m:
        print(m.groups())
        file_name = m.group(1)
        if m.group() == " /":
            file_name = "/index.html"
            

    print(file_name)
    # 2.0 返回给新用户返回数据
    # 2.1 设置状态行
    response_header = "HTTP/ 200 OK\r\n"
    response_header += "\r\n"
    # 2.0 设置响应体
    # print(file_name)
    try:
        f = open("moban3382/{}".format(file_name.lstrip()),"rb")
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
        new_client.send(response_header.encode("utf-8"))

        # 返回响应内容
        new_client.send(response_body)


    # 关闭新用户
    new_client.close()


def main():
    """
    主程序
    """
    # 1.0 创建tcp 套接字
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 1.1 套接字设置
    tcp_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    # 2.0 绑定服务器
    addr = ("127.0.0.1",8080)
    tcp_socket.bind(addr)

    # 3.0 监听用户
    tcp_socket.listen(128)

    while True:
          # 4.0 while True 接收新用户
        new_client,addr = tcp_socket.accept()

        # 5.0 处理新用户
        service_recv(new_client,addr)

    # 8.0 关闭总套接字
    tcp_socket.close()

if __name__ == '__main__':
    main()