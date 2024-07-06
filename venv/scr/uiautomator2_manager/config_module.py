# -*- coding: utf-8 -*-
"""
-
Author:
Date:
"""
from ntp_util import timestamp_to_date
import os
import ctypes


def get_desktop_path():
    # 使用 ctypes 调用 shell32.dll 获取桌面路径
    SHGetFolderPath = ctypes.windll.shell32.SHGetFolderPathW
    path = ctypes.create_unicode_buffer(260)
    # CSIDL_DESKTOP = 0 表示桌面
    SHGetFolderPath(None, 0, None, 0, path)
    return path.value


class ConfigManagerRUIBOSHI:
    # PAGE_ELEMENT_FILE_PATH = r'C:\Users\Administrator\PycharmProjects\AutoDriver_UIA2\venv\data\页面组件列表.xlsx'
    PAGE_ELEMENT_FILE_PATH = r'C:\Users\Administrator\PycharmProjects\AutoDriver_UIA2\venv\data\睿博士.xlsx'
    ADJACENCY_LIST = '邻接表'
    TRUST_LEVEL_TABLE = '置信表'
    # app包名
    APP_PACKAGE_NAME = 'com.zwcode.p6slite'
    # app活动名
    APP_ACTIVITY_NAME = '.activity.SplashActivity'
    # 所有列名
    TABLE_HEADERS = ['页面名称', '相邻页面', 'resource-id', 'bounds', 'text', '控件类型', '默认值', '置信度',
                     '等待时间']
    # 判断置信度的列名
    ATTRIBUTE_LIST = ['text', 'resource-id']
    # 所有元素类型
    UI_CONTROLS_TYPE = ['按钮', '文本框', '勾选框', '单选按钮', '空值', '持续到页面跳转', '截图']
    # 需要输入内容的元素
    UI_ELEMENTS = ['文本框', '单选按钮', '截图']
    # 截图保存路径
    SCREENSHOT_PATH = rf"C:\Users\Administrator\Desktop\video\截图"
    # 存储手机截屏路径
    MOBILE_SCREEN_CAPTUREA = '/sdcard/DCIM/Screenshots/'
    # 日志目录
    # 日志目录
    LOGS_DIR = f"{get_desktop_path()}/logs"


class ConfigManagerTest:
    # PAGE_ELEMENT_FILE_PATH = r'C:\Users\Administrator\PycharmProjects\AutoDriver_UIA2\venv\data\页面组件列表.xlsx'
    PAGE_ELEMENT_FILE_PATH = r'C:\Users\Administrator\PycharmProjects\AutoDriver_UIA2\venv\data\test.xlsx'
    ADJACENCY_LIST = '邻接表'
    TRUST_LEVEL_TABLE = '置信表'
    APP_PACKAGE_NAME = 'com.zwcode.p6slite'
    APP_ACTIVITY_NAME = '.activity.SplashActivity'
    TABLE_HEADERS = ['页面名称', '相邻页面', 'resource-id', 'bounds', 'text', '控件类型', '默认值', '置信度',
                     '等待时间']
    ATTRIBUTE_LIST = ['text', 'resource-id']

if __name__ == "__main__":
    print(get_desktop_path())
    print(ConfigManagerRUIBOSHI.LOGS_DIR)