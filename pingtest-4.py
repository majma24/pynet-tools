#!/usr/bin/env python

import os
import ipaddress
ping_result = open("ping-result.txt" , "w")
net_addr = input("Enter Your IP with CIDR (ex: 192.168.10.1/24) : " )
ip_addr = ipaddress.ip_network(net_addr, strict=False)
all_host = list(ip_addr.hosts())

for ip in all_host:
    ip = str(ip)
    output = os.system(f"ping -c 1 -w 1 {ip}")
    if output == 0:
        print(f"{ip} is Online")
        ping_result.writelines(f"{ip} is Online \n")
    else:
        print(f"{ip} is Offline")
        ping_result.writelines(f"{ip} is Offline \n")