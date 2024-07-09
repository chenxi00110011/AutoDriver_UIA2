# -*- coding: utf-8 -*-

import os
from tqdm import tqdm
import time
from my_decorator import schedule_task
import schedule

if __name__ == '__main__':

    for i in tqdm(range(9999)):
        os.system('test_case -vs -m aov_core_oppo')
