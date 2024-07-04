# -*- coding: utf-8 -*-
"""
-
Author:
Date:
"""
import time

from uiautomator2 import connect, Device

# 连接设备，这里使用设备的序列号，如果你没有提供序列号，将连接第一台可用的设备
device = connect('H675FIS8JJU8AMWW')

# 启动应用，假设应用包名为 'com.example.myapp'
device.app_start('com.zwcode.p6slite')
time.sleep(2)
# 点击屏幕上的某个元素，假设它的 resource-id 是 'com.example.myapp:id/my_button'
device(resourceId='com.zwcode.p6slite:id/device_set').click()
#
# # 等待一段时间，让应用有时间响应点击事件
# device.sleep(2)
#
# # 获取屏幕上某个元素的文本，假设它的 resource-id 是 'com.example.myapp:id/my_text_view'
# text = device(resourceId='com.example.myapp:id/my_text_view').text
#
# # 打印获取到的文本
# print("Text on the screen: ", text)
#
# # 断言验证文本是否符合预期
# assert "Expected Text" in text, "Text did not match the expected value"
#
# # 关闭应用
# device.app_stop('com.example.myapp')