# -*- coding: utf-8 -*-
# @Author: BigHead


import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from core import src
from lib import common_log

logger = common_log.get_logger(__name__)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

if __name__ == "__main__":
    # 定义 RDS 需要查询的 Key
    try:
        src.run('MySQL_Sessions,MySQL_InnoDBDataReadWriten,MySQL_InnoDBBufferRatio,MySQL_QPSTPS')
    except Exception as e:
        logger.error(e)
