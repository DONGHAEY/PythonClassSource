from socket import *

s_ip = '10.150.149.31'
s_port = 8080

s_socket = socket(AF_INET, SOCK_DGRAM)
s_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s_socket.bind((s_ip, s_port))

data, c_addr = s_socket.recvfrom(1024)

while data.decode('utf-8') != 'q' :
    print('Request from', c_addr)
    print('Data', data.decode('utf-8'))
    print()
    s_socket.sendto(data, c_addr)
    data, c_addr = s_socket.recvfrom(1024)

s_socket.close()
