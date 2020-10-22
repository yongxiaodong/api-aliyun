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
    # 加载配置文件
    from conf import settings
    # # 定义 RDS 需要查询的 Key, web网页暴露给Prometheus
    # try:
    #     src.run('MySQL_Sessions,MySQL_InnoDBDataReadWriten,MySQL_InnoDBBufferRatio,MySQL_QPSTPS')
    # except Exception as e:
    #     logger.error(e)

    # 获取资源组id
    # src.getresourcegroups(settings)

    # 创建ssh key
    # src.createkeypair(settings)

    instanceid = ["i-2vc3rc6kx8zid1eluhku"]
    # 将sshkey 绑定到实例
    # src.attachkeypair(settings, instanceid)
    # 重启实例，使绑定的sshkey生效，生效后将禁用用户名密码登录
    # src.rebootinstance(settings, instanceid[0])

    # 解绑ssh key
    src.detachkeypair(settings, instanceid)
    # # 重启实例，使解绑，生效后将启用用户名密码登录
    src.rebootinstance(settings, instanceid[0])

    # src.describeinstances(settings)
