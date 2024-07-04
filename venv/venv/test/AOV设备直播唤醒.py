# -*- coding: utf-8 -*-
"""
-
Author:
Date:
"""
import time
from uiautomator2_manager import uiautomator2_extended
from tqdm import tqdm
import time
from uiautomator2_extended import Uiautomator2SophisticatedExecutor
import pytest
import ntp_util
from loguru import logger
from config_module import ConfigManagerRUIBOSHI as rui

logger.add(rui.LOGS_DIR + f"\\{ntp_util.timestamp_to_date()}.log", encoding="utf-8")

# delay_list = [60, 120, 300, 600]
users = ["18086409233", "13638601129"]
sleep_time = 5
dids = ['000602', '000632']
qualitys = ['超清', '高清', '流畅']
combinations = [(did, quality) for quality in qualitys for did in dids]
logger.info(combinations)
wake_up_times = {'直播唤醒': [],
                 '设置唤醒': []}
did = dids[0]
quality = qualitys[0]


for i in tqdm(range(100)):
    app = uiautomator2_extended.Uiautomator2SophisticatedExecutor('H675FIS8JJU8AMWW', 'com.zwcode.p6slite')
    logger.info(f"设备休眠时间为{sleep_time}秒")
    time.sleep(sleep_time)
    app.did = did
    start_time = time.time()
    app.go_to_page("直播", did)
    count = 0
    while not app.exists_element(value="云台"):
        count += 1
        if count >= 30:
            logger.error("直播预览出流超时")
            break
        logger.info("未检测到设备出流")
    end_time = time.time()
    wake_up_time = end_time - start_time
    wake_up_times['直播唤醒'].append(wake_up_time)
    logger.debug("***********************进入直播用时{:.2f}秒**********************".format(wake_up_time))
    logger.debug([num for num in wake_up_times['直播唤醒'] if num <= 30])
    app.go_to_page("切换画质", quality)
    time.sleep(5)
    app.go_to_page("截图")