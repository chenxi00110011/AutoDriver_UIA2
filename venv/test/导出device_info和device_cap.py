# -*- coding: utf-8 -*-
"""
-
Author:
Date:
"""
from xrs_cgi import getDeviceInfo, getDeviceCap

ip = "192.168.123.190"
print(getDeviceInfo(ip))
print(getDeviceCap(ip))