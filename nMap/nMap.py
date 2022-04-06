import nmap

targethost = '10.150.149.31'
nmScan = nmap.PortScanner()
nm = nmScan.scan(targethost, '22-80')

print(nm);print()
print(nm['nmap']);print()
print(nm['scan']);print()
print(nm['scan']['192.168.35.211']);print()
print(nm['scan']['192.168.35.211']['status']);print()
print(nm['scan']['192.168.35.211']['addresses']);print()