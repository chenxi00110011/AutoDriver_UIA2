# -*- coding: utf-8 -*-
"""
-
Author:
Date:
"""
import time
from uiautomator2_manager import uiautomator2_extended
from device_api import DeviceAPIManager
from arp_scan import get_ip
from xrs_serial import serial_bitstream
from tqdm import tqdm


def case01():
    mac = "5A:5A:00:6B:5A:EA"
    com = "com38"
    serial_bitstream(com, '断电', 10)
    serial_bitstream(com, '上电', 60)
    ip = get_ip(mac)
    if ip:
        api = DeviceAPIManager(ip)
        api.reset_to_factory_settings()
        time.sleep(60)
    d = uiautomator2_extended.Uiautomator2SophisticatedExecutor('H675FIS8JJU8AMWW', 'com.zwcode.p6slite')
    d.go_to_page('蓝牙-设备连接中', 'IOTFAA-033127-FFXBL')
    d.go_to_page('设备添加成功')
    d.go_to_page('首页')


if __name__ == '__main__':
    for i in tqdm(range(100)):
        case01()
