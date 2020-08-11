# -*- coding: utf-8 -*-
# @Author: BigHead


from conf import settings
import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# logging.basicConfig(filename=settings.BASE_DIR, level=logging.DEBUG, format=LOG_FORMAT)

logging.basicConfig(filename=settings.BASE_DIR,format='[%(levelname)s %(asctime)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)

from conf import settings

# import time
#
# def loging(msg):
#     with open(settings.LOG_PATH, 'a', encoding='utf-8') as f:
#         f.write("%s %s\n" %(time.strftime('%Y-%m-%d %H:%M:%S'),msg))



def info(msg):
    logging.info(msg)


def error(msg):
    logging.error(msg)
