# -*- coding: utf-8 -*-
"""
-
Author:
Date:
"""
import time
from uiautomator2_extended import Uiautomator2SophisticatedExecutor
import pytest
import ntp_util
from loguru import logger
from config_module import ConfigManagerRUIBOSHI as rui

logger.add(rui.LOGS_DIR + f"\\{ntp_util.timestamp_to_date()}.log", encoding="utf-8")

# delay_list = [60, 120, 300, 600]
users = ["18086409233", "13638601129"]
sleep_time = 30
dids = [
        '家24',
        '卧室23',
        '深圳设备1',
        '深圳设备2'
]
qualitys = [
            '超清',
            '高清',
            '流畅'
            ]
combinations = [(did, quality) for quality in qualitys for did in dids]
logger.info(combinations)
wake_up_times = {'直播唤醒': [],
                 '设置唤醒': []}


@pytest.mark.aov_core_oppo
@pytest.mark.parametrize("did, quality", combinations)
@pytest.mark.repeat(1)
def test_pull_live_stream(did: str, quality: str, setup_ruiboshi: Uiautomator2SophisticatedExecutor):
    logger.info(f"设备休眠时间为{sleep_time}秒")
    time.sleep(sleep_time)
    app = setup_ruiboshi
    app.did = did
    app.go_to_page("首页", '13590267955', 'ljf123456')
    start_time = time.time()
    app.go_to_page("直播", did)
    if app.exists_element(value='提示'):
        print("检测到提示")
        time.sleep(5.0)
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
    app.title['wakeup_time'] = "{:.2f}".format(wake_up_time)
    time.sleep(2)
    app.go_to_page("切换画质", quality)
    time.sleep(5)
    app.go_to_page("截图")
    wake_up_list = [num for num in wake_up_times['直播唤醒'] if num <= 30]
    logger.debug(wake_up_list)
    logger.debug(sum(wake_up_list) / len(wake_up_list))
    app.go_to_page("回放")
    time.sleep(10)
    app.go_to_page("截图")
    app.app_stop_()

#
# @test_case.mark.aov_core_oppo
# @test_case.mark.parametrize("did", dids)
# @test_case.mark.repeat(1)
# def test_open_settings_page(did: str, setup_ruiboshi: Uiautomator2SophisticatedExecutor):
#     logger.info(f"设备休眠时间为{sleep_time}秒")
#     time.sleep(sleep_time)
#     app = setup_ruiboshi
#     app.did = did
#     start_time = time.time()
#     app.go_to_page("设备设置", did)
#     while app.exists_element(selector="text", value='提示'):
#         time.sleep(5)
#     count = 0
#     while not app.exists_element(value="工作模式"):
#         count += 1
#         if count >= 30:
#             logger.error("进入设置页面超时")
#             break
#         logger.info("未进入设置页面")
#     end_time = time.time()
#     wake_up_time = end_time - start_time
#     wake_up_times['设置唤醒'].append(wake_up_time)
#     logger.debug("***********************进入设置页面用时{:.2f}秒**********************".format(wake_up_time))
#     logger.debug(wake_up_times['设置唤醒'])
#     app.go_to_page("翻转")
#     app.app_stop_()
#
