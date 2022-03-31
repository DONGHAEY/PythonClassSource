from socket import *

s_ip = 'localhost'
s_port = 9999

c_socket = socket(AF_INET, SOCK_STREAM)

c_socket.connect((s_ip, s_port))

print('data', c_socket.recv(1024).decode('utf-8'))

c_socket.send('Hello, TCP SERVER!!'.encode('utf-8'))

c_socket.close()