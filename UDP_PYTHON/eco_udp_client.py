from socket import *

s_ip = '10.150.149.31'
s_port = 8080

c_sock = socket(AF_INET, SOCK_DGRAM)

inputData = input('Enter String')
c_sock.sendto(inputData.encode('utf-8'), (s_ip, s_port))
while inputData != 'q' :
    data, addr = c_sock.recvfrom(1024)
    print('data : ', data.decode('utf-8'))
    inputData = input('Enter String : ')
    c_sock.sendto(inputData.encode('utf-8'), (s_ip, s_port))

c_sock.close()