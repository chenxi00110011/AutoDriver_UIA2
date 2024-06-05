# -*- coding: utf-8 -*-
"""
-
Author:
Date:
"""
import time

from arp_scan import get_ip
from tqdm import tqdm
from xrs_serial import serial_bitstream
from telnet_client import telnet_connect
from device_api import DeviceAPIManager


def fun(mac):
    host = get_ip(mac)
    DeviceAPIManager(host).open_telnet()
    username = "root"
    password = "zviewa5s"
    command = "route -n"
    telnet_connect(host, username, password, command)


mac = 'B4:6D:C2:FE:1C:CE'
com = 'com38'
for t in tqdm(range(1000)):
    serial_bitstream(com, '断电', 20)
    fun(mac)
    serial_bitstream(com, '上电', 20)
    fun(mac)