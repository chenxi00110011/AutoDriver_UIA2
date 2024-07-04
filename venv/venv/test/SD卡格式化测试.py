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
        DeviceAPIManager(f'http://{ip}').dev_reboot()

    time.sleep(120)

    for mac in macList:
        print(mac)
        ip = get_ip(mac)
        # 获取SD卡信息
        dev = DeviceAPIManager(f'http://{ip}')
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
        dev = DeviceAPIManager(f'http://{ip}')
        tmp = dev.get_sdcard_info()
        print(tmp['DiskList']['Disk']['DiskStorageAttribute'])
        assert tmp['DiskList']['Disk']['DiskStorageAttribute'] == 'writting'


if __name__ == '__main__':
    mac_list = ['5A:5A:00:6B:5A:D1',
                # '5A:5A:00:6B:59:22',
                # '5A:5A:00:6B:5B:1D',
                '5A:5A:00:6B:5A:DF']
    for i in tqdm(range(300)):
        test_sd_format(mac_list)
