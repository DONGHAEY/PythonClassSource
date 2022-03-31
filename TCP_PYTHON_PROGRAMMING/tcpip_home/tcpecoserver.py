from socket import *

s_ip ='localhost'
s_port = 8888

s_socket = socket(AF_INET, SOCK_STREAM)
s_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #끊어지지 않고 재사용을 하겠다
s_socket.bind((s_ip, s_port))
s_socket.listen(2)

client, c_addr = s_socket.accept()
print(c_addr, 'is connected')

data = 'dummy'

while len(data) :
    data = client.recv(1024).decode('utf-8')
    print('recieved data : ', data)
    client.send(data.encode('utf-8'))

client.close()
s_socket.close()