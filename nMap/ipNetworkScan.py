from socket import *

net = input('Network ID (ex:192.168.32) : ')

start = int(input('Start host ID : '))
end = int(input('Last host ID : '))
port = int(input('Port Number'))

ipscan_sock =socket(AF_INET, SOCK_STREAM)

def scan(addr) :
    ipscan_sock = socket(AF_INET, SOCK_STREAM)
    setdefaulttimeout(1)
    result = ipscan_sock.connect_ex((addr,port))

    if result == 0 :
        return 1
    else :
        return 0

def run() :
    for ip in range(start, end+1) :
        addr = net+'.' + str(ip)
        print(addr)
        if (scan(addr)) :
            print('is live', end='')
        else :
            print('is not live')
        ipscan_sock.close()

run()