# -*- coding: utf-8 -*-
# @Author: BigHead

import os

# 如果没有redisID 或则rdsid 写 None

# 阿里云accessID,获取方法 https://help.aliyun.com/knowledge_detail/38738.html
accessKeyId = 'accesskey'
# 阿里云secret，获取方法 https://help.aliyun.com/knowledge_detail/38738.html
accessSecret = 'secret'
# 服务器区域
zone = 'cn-chengdu'
#rds的实例id
rds1 = 'rm-id'
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# redis的实例id
REDIS_ID = 'r-id'
