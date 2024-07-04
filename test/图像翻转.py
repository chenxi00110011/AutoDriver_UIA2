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
did = '000602'
app = uiautomator2_extended.Uiautomator2SophisticatedExecutor('H675FIS8JJU8AMWW', 'com.zwcode.p6slite')
start_time = time.time()
app.go_to_page("设备设置", did)
while app.exists_element(selector="text", value='提示'):
    time.sleep(5)
count = 0
while not app.exists_element(value="运动检测"):
    count += 1
    if count >= 30:
        logger.error("进入设置页面超时")
        break
    logger.info("未进入设置页面")
end_time = time.time()
wake_up_time = end_time - start_time
# wake_up_times['设置唤醒'].append(wake_up_time)
# logger.debug("***********************进入设置页面用时{:.2f}秒**********************".format(wake_up_time))
# logger.debug(wake_up_times['设置唤醒'])
app.go_to_page("翻转")
