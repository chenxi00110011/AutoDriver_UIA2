# -*- coding: utf-8 -*-
"""
-
Author:
Date:
"""
from device_api import DeviceAPIManager
import time
from arp_scan import get_ip
from my_decorator import print_current_time
from tqdm import tqdm


# @threading_decorator
@print_current_time
def test_sd_format(macList: list):
    for mac in macList:
        ip = get_ip(mac)
        # 设备重启
        DeviceAPIManager(f'{ip}').dev_reboot()

    time.sleep(120)

    for mac in macList:
        print(mac)
        ip = get_ip(mac)
        # 获取SD卡信息
        dev = DeviceAPIManager(f'{ip}')
        tmp = dev.get_sdcard_info()
        print(tmp['DiskList']['Disk']['DiskStorageAttribute'])
        assert tmp['DiskList']['Disk']['DiskStorageAttribute'] == 'writting'
        # 格式化SD卡
        dev.format_sdcard()

    time.sleep(60)

    for mac in macList:
        print(mac)
        ip = get_ip(mac)
        # 获取SD卡信息
        dev = DeviceAPIManager(f'{ip}')
        tmp = dev.get_sdcard_info()
        print(tmp['DiskList']['Disk']['DiskStorageAttribute'])
        assert tmp['DiskList']['Disk']['DiskStorageAttribute'] == 'writting'


if __name__ == '__main__':
    mac_list = ['5A:00:55:F1:7B:7E',
                '5A:00:65:85:ED:82',
                '5A:00:7A:A0:F5:D5',
                '5A:5A:00:83:78:B0'
                ]
    for i in tqdm(range(20)):
        test_sd_format(mac_list)
