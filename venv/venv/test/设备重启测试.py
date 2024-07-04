# -*- coding: utf-8 -*-
"""
-
Author:
Date:
"""
from arp_scan import all_islive
from tqdm import tqdm
from xrs_serial import serial_bitstream
import time

mac_list = ['5A:5A:00:5C:3D:62']
com = 'com38'
for t in tqdm(range(300)):
    serial_bitstream(com, '断电', 10)
    serial_bitstream(com, '上电', 120 - 10)
    if all_islive(mac_list):
        print('#' * 10, '检测到设备', '#' * 10)
    else:
        print('*' * 10, '未检测到设备', '*' * 10)
        time.sleep(1000_000)

