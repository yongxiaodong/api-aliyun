# -*- coding: utf-8 -*-
# @Author: BigHead
import sys
import os
import time
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

if not os.path.exists("%s/logs" %BASE_DIR):
    os.mkdir("%s/logs" %BASE_DIR)

from core import src


if __name__ == "__main__":
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    src.run()

