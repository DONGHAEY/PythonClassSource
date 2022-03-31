from socket import *
s_ip = 'localhost'
s_port = 8888

c_socket = socket(AF_INET, SOCK_STREAM)

c_socket.connect((s_ip, s_port))
while(True) :
    inputdata = input('enter data')
    c_socket.send(inputdata.encode('utf8'))
    print(c_socket.recv(1024).decode('utf-8'))
    if inputdata =='q' :
        break

c_socket.close()