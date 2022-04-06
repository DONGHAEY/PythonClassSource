import nmap

targethost = '10.150.149.31'
nmScan = nmap.PortScanner()
nm = nmScan.scan(targethost, '22-80')