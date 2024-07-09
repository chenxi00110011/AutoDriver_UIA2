# -*- coding: utf-8 -*-
"""
-
Author:
Date:
"""
from xrs_cgi import all_open_telnet
from telnet_client import telnet_connect

ips = ['192.168.123.130',
       '192.168.123.123',
       '192.168.123.128']
all_open_telnet(ips)

host = ips[0]
username = "root"
password = ""
command = """
mount /dev/mmcblk0p1 /dat/;
cd /dat/picture/;
chmod 777 iotest;
./iotest;
"""
telnet_connect(host, username, password, command)


