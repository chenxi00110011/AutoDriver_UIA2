# -*- coding: utf-8 -*-

import os
import time
from my_decorator import schedule_task
import schedule

if __name__ == '__main__':

    for i in range(9999):
        os.system('pytest -vs -m aov_core_oppo')
