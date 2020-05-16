#!/usr/bin/env python
import subprocess
import ipaddress


ping_result = open("ping-result.txt" , "w")
net_addr = input("Enter Your IP with CIDR (ex: 192.168.10.1/24) : " )
ip_addr = ipaddress.ip_network(net_addr, strict=False)
all_host = list(ip_addr.hosts())

for ip in all_host:
    #output = subprocess.Popen(["ping" , "-c 1" , str(ip)], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output = subprocess.Popen(["ping" , "-c 1" , str(ip)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = output.communicate()
    #print(output)
    if (output.returncode == 0):
        print(f"{ip} is UP")
        ping_result.writelines(f"{ip} is UP \n")
    else:
        print(f"{ip} is DOWN")
        ping_result.writelines(f"{ip} is DOWN \n")
 