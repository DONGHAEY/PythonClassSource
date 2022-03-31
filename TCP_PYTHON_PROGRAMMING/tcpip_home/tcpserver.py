from socket import *

s_ip = 'localhost' # 172.0.0.1
s_port = 9999

s_socket = socket( AF_INET, SOCK_STREAM)
#AF_INET - IPV4, SOCK_STREAM -TCP를 만들겠다

#bind
s_socket.bind((s_ip, s_port))
#listen
s_socket.listen(2)

client, c_addr = s_socket.accept()

print(c_addr, 'is connected')

client.send('Thankyou'.encode('utf-8'))

print('data', client.recv(1024).decode('utf-8'))

client.close()
s_socket.close()
