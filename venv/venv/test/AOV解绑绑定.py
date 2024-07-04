# -*- coding: utf-8 -*-
"""
-
Author:
Date:
"""
import time

import ntp_util
from uiautomator2_manager import uiautomator2_extended
from tqdm import tqdm
from loguru import logger
from config_module import ConfigManagerRUIBOSHI as rui

logger.add(rui.LOGS_DIR + f"\\{ntp_util.timestamp_to_date()}.log", encoding="utf-8")

for i in tqdm(range(2)):
    app = uiautomator2_extended.Uiautomator2SophisticatedExecutor('H675FIS8JJU8AMWW', 'com.zwcode.p6slite')
    wake_up_times = {'直播唤醒': [],
                     '设置唤醒': []}
    time.sleep(5)
    sleep_time = 10
    did = '000602'
    quality = '超清'
    logger.info(f"设备休眠时间为{sleep_time}秒")
    time.sleep(sleep_time)
    app.did = did
    start_time = time.time()
    app.go_to_page("直播", did)
    if app.exists_element(value='提示'):
        time.sleep(6.0)
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
    wake_up_list = [num for num in wake_up_times['直播唤醒'] if num <= 30]
    logger.debug(wake_up_list)
    logger.debug(sum(wake_up_list) / len(wake_up_list))
    app.title['wakeup_time'] = "{:.2f}".format(wake_up_time)
    app.go_to_page("切换画质", quality)
    time.sleep(5)
    app.go_to_page("截图")
