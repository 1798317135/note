import socket

tcp_socket = socket.socket()

tcp_socket.bind(("127.0.0.1",8080))

tcp_socket.listen(128)

# 设置套接字为非阻塞
tcp_socket.setblocking(False)
client_list = list()
while True:
    try:
        new_client,addr = tcp_socket.accept()
    except Exception as e:
        pass
    else:
        new_client.setblocking(False)
        client_list.append(new_client)

    for client in client_list:
        try:
            recv_data = client.recv(1024)
        except Exception as e:
            pass
        else:
            if recv_data:
                print(recv_data)
                
               
            new_client.close()
            client_list.remove(client)

tcp_socket.close()



            

