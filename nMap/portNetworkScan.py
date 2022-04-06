from socket import *

target_ip = input('enter another ip  : ')
start_port = int(input('enter start port : '))
end_port = int(input('enter finish port : '))

try:
    for port in range(start_port, end_port) :
        ipscan_sock = socket(AF_INET, SOCK_STREAM)
        ipscan_sock.settimeout(.5)
        result = ipscan_sock.connect_ex((target_ip, port))
        if result == 0 :
            print('opend at ', port)
        ipscan_sock.close()
except KeyboardInterrupt:
    print("this program is finished")

except gaierror :
    print("hostname is not found")

print("Scaning is finished")
