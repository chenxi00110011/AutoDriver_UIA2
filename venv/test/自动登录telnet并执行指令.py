# -*- coding: utf-8 -*-
"""
-
Author:
Date:
"""
from telnet_client import telnet_connect
from xrs_cgi import open_telnet
from arp_scan import get_ip

# 设置Telnet服务器的信息
mac_list = [
    '5A:5A:00:5C:3D:62',
    '5A:5A:00:7E:FF:DF'
]

host_list = [
    '192.168.123.179',
    '192.168.20.135'
]

if not host_list:
    for mac in mac_list:
        host_list.append(get_ip(mac))
user = "root"
password = "zviewa5s"
commads = [
    'uptime'
]

for host in host_list:
    open_telnet(host)
    # 创建Telnet客户端实例
    print(f"设备ip: {host}")

    telnet_connect(host, user, password, commads)
    print("#" * 20 + "end" + "#" * 20)
