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


def ota():
    d = uiautomator2_extended.Uiautomator2SophisticatedExecutor('H675FIS8JJU8AMWW', 'com.zwcode.p6slite')
    d.go_to_page('设备设置')
    d.go_to_page('立即升级')


if __name__ == '__main__':
    ota()
