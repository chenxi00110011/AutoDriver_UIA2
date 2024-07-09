# -*- coding: utf-8 -*-
"""
-
Author:
Date:
"""
from tqdm import tqdm
from arp_scan import all_islive
from xrs_serial import serial_bitstream
from arp_scan import get_ip
from device_api import DeviceAPIManager

mac_list = ['34:7D:E4:9D:4B:9A']
com = 'com38'
time_dict = {60: 1,
             120: 1,
             300: 10,
             600: 10,
             3600: 4,
             7200: 2}

serial_bitstream(com, '上电', 60)

for k in time_dict.keys():
    for i in tqdm(range(time_dict[k])):
        ip = get_ip('34:7D:E4:9D:4B:9A')
        cgi = DeviceAPIManager(ip)
        cgi.dev_reboot()
        serial_bitstream(com, '断电', k)
        serial_bitstream(com, '上电', 120)
        if all_islive(mac_list):
            print('#' * 10, '检测到设备', '#' * 10)
        else:
            print('*' * 10, '未检测到设备', '*' * 10)
